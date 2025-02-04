from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def generate_advice(request):
    '''
    Creates an AI-generated advice based on user input.
    '''
    data = request.data

    print("##################")
    print(data)
    print("##################")

    return Response({'success': True,
                     'detail': 'Form was submitted successfully!',
                     'status': status.HTTP_200_OK})
