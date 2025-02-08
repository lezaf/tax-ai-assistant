from backend.settings import env

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from openai import OpenAI

from .utils import (
    _create_or_update_history,
    _set_user_id_session_attribute,
    _create_user_content)
from .models import ChatHistory

client = OpenAI(
    api_key=env('OPENAI_API_KEY')
)


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
    user_content = _create_user_content(data['userData'], data['userPrompt'])
    
    # Get the model
    chat, _ = ChatHistory.objects.get_or_create(user_id=user_id)
    _create_or_update_history(chat,
                              role="user",
                              content=user_content)

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
    _create_or_update_history(chat,
                              role="assistant",
                              content=chat_completion.choices[0].message.content)
    print(chat.messages)
    chat.save()

    return Response({
        'success': True,
        'detail': 'Form was submitted successfully!',
        'answer': chat_completion.choices[0].message.content
        },
        status=status.HTTP_200_OK)
