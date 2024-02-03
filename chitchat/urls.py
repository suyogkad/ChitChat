from django.contrib import admin
from django.urls import path, include  # include is important for including app-specific urls
from chat.views import home  # Add this import
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', home, name='home'),  # Add this line for the homepage
    # path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
]


