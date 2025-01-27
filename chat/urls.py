from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/<str:username>/', views.get_messages, name='chat_user'),
]
