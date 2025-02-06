from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from rest_framework import status


# Mock classes to mimic OpenAI response
class MockMessage:
    def __init__(self, content):
        self.content = content

class MockChoices:
    def __init__(self, content):
        self.message = MockMessage(content)

class MockOpenAIResponse:
    def __init__(self, content):
        self.choices = [MockChoices(content)]

class GenerateAdviceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/advice/generate'

        self.valid_data = {
            "userData": {
                "income": "20000",
                "expenses": "3000",
                "propertiesNum": "2"
            },
            "userPrompt": "What will be my taxes living in Brazil?"
        }

    @patch("advice.views.client.chat.completions.create")
    def test_generate_advice_success(self, mock_openai):
        '''
        Tests backend API returns successful response when
        OpenAI call is successful.
        '''
        mock_openai.return_value = MockOpenAIResponse("Given that you live in Brazil the...")

        # Make the backend API call
        response = self.client.post(self.url, self.valid_data, format="json")

        self.assertTrue(response.data["success"])
        self.assertIn("answer", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generate_advice_missing_user_prompt(self):
        '''Test API response when userPrompt is missing.'''

        invalid_data = {
            "userData": {
                "income": "20000",
                "expenses": "3000",
                "propertiesNum": "2"
            }
        }

        response = self.client.post(self.url, invalid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_generate_advice_missing_user_data(self):
        '''Test API response when userData is missing.'''

        invalid_data = {
            "userData": "What will be my taxes living in Brazil?"
        }

        response = self.client.post(self.url, invalid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("advice.views.client.chat.completions.create")
    def test_generate_advice_openai_error(self, mock_openai):
        '''Tests OpenAI call fails.'''
        mock_openai.side_effect = Exception("OpenAI API error.")

        # Make the backend API call
        response = self.client.post(self.url, self.valid_data, format="json")

        self.assertFalse(response.data["success"])
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)