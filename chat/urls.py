from django.urls import path
from .views import message_list  # Import the view
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('messages/', message_list, name='message_list'),  # URL path for the message list view
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='/chat/login/'), name='logout'),
    path('logout/', views.custom_logout, name='logout'),
    # Ensure the login URL is correctly defined as well
]