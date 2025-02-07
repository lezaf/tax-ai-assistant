# Tax AI assistant

Welcome to the **Tax AI Assistant**, an AI-driven web application that ingest the tax data you provide along with a question and give you valuable advice! :rocket: The project will be developed incrementally with documentation for the underlying technologies and techniques. Keep reading to learn the individual parts consisting the app. :pencil2:

## Frontend - Vue3 + Vite

<p align="center">
<img src="https://vuejs.org/images/logo.png" alt="Vue Logo" width="50" height="50"> + <img src="https://vite.dev/logo.svg" alt="Vite Logo" width="50">
</p>

The frontend of the application is developed in **Vue3** (Composition API) + **Vite**, the default building tool for Vue applications.

To build and run the frontend server in dev mode run:

```
cd frontend
npm install
npm run dev
```

## Backend - django + DRF

<p align="center"><img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" width="100"> &nbsp + <img src="https://www.django-rest-framework.org/img/logo.png" width="100">
</p>

The backend is developed in **django** + **django REST framework** and **Python 3.13.1**. To build the backend create a virtual environment for python and use [requirements](./backend/requirements.txt) file to install necessary dependencies:

```
# Using PyPI
pip install -r requirements.txt
```

### Local .env file

Create a local **.env** to store environment variables. The file is excluded from tracking (see [.gitignore](./backend/.gitignore)). Use [.env.template](./backend/.env.template) as a template. Variables declared in .env include:

```
DEBUG=on
SECRET_KEY=my_django_secret_key
OPENAI_API_KEY=my_openai_key
```

### API endpoints

Below is the backend API endpoints documentation:

| method |      endpoint       | description                                         |
| :----: | :-----------------: | :-------------------------------------------------- |
|  POST  | api/advice/generate | Generates AI response based on user data and prompt |

## AI integration using OpenAI

To integrate AI in backend to generate content based on prompts, the [OpenAI Python API library](https://github.com/openai/openai-python) is used. Backend app [advice](./backend/advice) is responsible for handling AI-related API calls. To generate tax filing advice, **generate_advice** view is called to communicate with OpenAI API:

```
# in backend/advice/views.py

# ...

client  =  OpenAI(
api_key=env('OPENAI_API_KEY')

@api_view(['POST'])
def  generate_advice(request):
    # ...

    try:
        chat_completion  =  client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful tax filing assistant." +
                        "You get tax related data and a user prompt"  +
                        "and you provide advice."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
        )

# ...
```

In this part, the OpenAI client is created and the expected behavior is defined. On success, the **AI generated answer** is included in _Response_:

```
# in backend/advice/views.py

# ...

@api_view(['POST'])
def  generate_advice(request):
    # ...

    return  Response({
        'success': True,
        'detail': 'Form was submitted successfully!',
        'answer': chat_completion.choices[0].message.content
    },
    status=status.HTTP_200_OK)
```

## Containerization with Docker

To build and operate app in Docker container:

- Prepare .env in backend (see [Local .env file](#local-env-file))
- **Build** and **start** the containers using [docker-compose.yml](./docker-compose.yml):

```
docker-compose up
```

Follow frontend's container url (by default http://localhost:5173) to operate application.

## CI pipeline

To ensure smooth **Continuous Integration** to the application, **GitHub Actions** workflows are used. In [.github/workflows](.github/workflows) there are workflows for backend and frontend parts. The workflows are defined for **push** and **pull request** to main.

#### Backend: django.yml

Handles backend build for specified versions, uses secrets stored in GitHub's _Actions Secrets and Variables_ to set necessary environment variables and install dependencies. Finally, runs specified tests with django testing environment.

#### Frontend: nodejs

Handles frontend build for specified versions, installs dependecies and runs specified tests with vitest environment.
