from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def message_list(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('message_list')
    else:
        form = MessageForm()

    messages = Message.objects.all()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': form})

def home(request):
    return HttpResponse('<h1>Welcome to ChitChat!</h1><p><a href="/chat/messages/">Go to Chat Messages</a></p>')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form': form})



