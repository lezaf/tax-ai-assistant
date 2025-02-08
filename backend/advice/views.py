import uuid
from backend.settings import env
from .models import ChatHistory

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from openai import OpenAI

client = OpenAI(
    api_key=env('OPENAI_API_KEY')
)

def _create_or_update_history(chat, user_prompt):
    '''
    Creates or updates the chat messages.

    If chat is empty, then it defines model behavior and guidelines.
    Else, it appends the current user prompt.
    '''
    # Define model behavior
    if not chat.messages:
        chat.messages.append(
            {
                "role": "developer",
                "content": "You are a helpful tax filing assistant. You get tax related data and " +
                        "a user prompt and you provide advice." +
                        "Keep your answers around 200 words." +
                        "If you are asked about something not related to taxes " +
                        "remind user politely that you are a tax filing assistant."
            }
        )
    
    # Add new user prompt
    chat.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

def _set_user_id_session_attribute(request):
    '''Creates a user id for the session.'''
    if 'user_id' not in request.session:
        request.session['user_id'] = str(uuid.uuid4())
        request.session.modified = True


@api_view(['POST'])
def generate_advice(request):
    '''
    Creates an AI-generated advice based on user input.
    '''
    data = request.data

    # Check request has necessary fields
    if 'userData' not in data:
        return Response({'detail': 'userData field is missing.'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if 'userPrompt' not in data:
        return Response({'detail': 'userPrompt field is missing.'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    # Create user in db if not exists
    _set_user_id_session_attribute(request)
    user_id = request.session['user_id']

    # Construct user's prompt
    user_data = data['userData']

    user_data_str = ", ".join(f"{k}= {user_data[k]}" for k in user_data)
    user_prompt = f"The user provided following data: {user_data_str}." \
                  f" User's message is : {data['userPrompt']}"
    
    # Get the model
    chat, _ = ChatHistory.objects.get_or_create(user_id=user_id)
    _create_or_update_history(chat, user_prompt)

    # API call to OpenAI
    try:
        chat_completion = client.chat.completions.create(
            model='gpt-4o',
            messages=chat.messages,
            temperature=0.3
        )
    except Exception as e:
        return Response({
            'success': False,
            'detail': str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Store new answer and save model
    chat.messages.append(
        {
            "role": "assistant",
            "content": chat_completion.choices[0].message.content
        }
    )
    chat.save()

    return Response({
        'success': True,
        'detail': 'Form was submitted successfully!',
        'answer': chat_completion.choices[0].message.content
        },
        status=status.HTTP_200_OK)
