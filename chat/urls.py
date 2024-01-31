from django.urls import path
from .views import message_list  # Import the view

urlpatterns = [
    path('messages/', message_list, name='message_list'),  # URL path for the message list view
]
