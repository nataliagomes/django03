from django.urls import path, include
from website.views import index, sobre , login

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('ideas'cadastrar_ideas), 
]
