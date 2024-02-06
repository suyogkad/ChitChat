from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import SignUpForm, MessageForm
from django.db.models import Q


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

def custom_logout(request):
    logout(request)
    return redirect('/chat/login/')  # Redirect to the login page


@login_required
def message_list(request, username=None):
    form = MessageForm()
    users = User.objects.exclude(id=request.user.id)

    selected_user = None
    messages = Message.objects.none()

    if username:
        selected_user = get_object_or_404(User, username=username)
        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=selected_user)) |
            (Q(sender=selected_user) & Q(receiver=request.user))
        ).order_by('timestamp')

        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                msg = form.save(commit=False)
                msg.sender = request.user
                msg.receiver = selected_user
                msg.save()
                return redirect('message_list', username=username)

    return render(request, 'chat/message_list.html', {
        'users': users,
        'messages': messages,
        'form': form,
        'selected_user': selected_user
    })

