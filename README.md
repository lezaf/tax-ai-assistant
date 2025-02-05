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

Create a local **.env** to store environment variables. The file is excluded from tracking (see [.gitignore](./backend/.gitignore)). Variables declared in .env include:

```
DEBUG=on
SECRET_KEY=my_django_secret_key
OPENAI_API_KEY=my_openai_key
```

### API endpoints

Below is the backend API endpoints documentation:

| method | endpoint            | description                                         |
| :----: | :------------------ | :-------------------------------------------------- |
|  POST  | api/advice/generate | Generates AI response based on user data and prompt |
