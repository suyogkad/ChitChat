from django.urls import path
from .views import message_list  # Import the view
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import message_list, signup, custom_logout

# url patterns
urlpatterns = [
    path('messages/', message_list, name='message_list'),  # URL path for the message list view
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('messages/<str:username>/', message_list, name='message_list_with_user'),
]