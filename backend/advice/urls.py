from django.urls import path
from . import views

urlpatterns = [
    path('api/advice/generate', views.generate_advice)
]