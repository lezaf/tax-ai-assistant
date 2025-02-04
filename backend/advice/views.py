from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import environ
from openai import OpenAI
from backend.settings import env

# Initialize environ

client = OpenAI(
    api_key=env('OPENAI_API_KEY')
)

@api_view(['POST'])
def generate_advice(request):
    '''
    Creates an AI-generated advice based on user input.
    '''
    data = request.data

    # Construct user's prompt
    user_data_str = ", ".join(f"{k}= {data[k]}" for k in data)
    user_prompt = f"The user provided following data: {user_data_str}." + f"Make a comment on this."

    # API call to OpenAI
    try:
        chat_completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful tax filing assistant. You get tax related data and" +
                            "a user request and you provide advice."
                            # Be friendly and keep your answers not very extensive.
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
        )

        print(chat_completion.choices[0].message.content)
    except Exception as e:
        return Response({
            'success': False,
            'detail': str(e),
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR
        })

    return Response({
        'success': True,
        'detail': 'Form was submitted successfully!',
        'status': status.HTTP_200_OK
        })
