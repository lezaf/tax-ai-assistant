from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from openai import OpenAI
from backend.settings import env

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

    user_data = data['userData']

    # Construct user's prompt
    user_data_str = ", ".join(f"{k}= {user_data[k]}" for k in user_data)
    user_prompt = f"The user provided following data: {user_data_str}." \
                  f" User's message is : {data['userPrompt']}"

    # API call to OpenAI
    try:
        chat_completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful tax filing assistant. You get tax related data and" +
                            "a user prompt and you provide advice." +
                            "Keep your answers around 200 words."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3
        )
    except Exception as e:
        return Response({
            'success': False,
            'detail': str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({
        'success': True,
        'detail': 'Form was submitted successfully!',
        'answer': chat_completion.choices[0].message.content
        },
        status=status.HTTP_200_OK)
