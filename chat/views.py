from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import SignUpForm, MessageForm


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


@login_required
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

    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)

    return render(request, 'chat/message_list.html', {
        'users': users, 'messages': messages.order_by('-timestamp'), 'form': form
    })