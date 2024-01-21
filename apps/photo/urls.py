from django.urls import path
from .views import  GenerateImageView

urlpatterns = [
    path('generate/api/',GenerateImageView.as_view()),
]