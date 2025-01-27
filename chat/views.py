from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from .forms import RegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def chat_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat.html', {'users': users})

@login_required
def get_messages(request, username):
    user = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, receiver=user) | \
               Message.objects.filter(sender=user, receiver=request.user)
    return render(request, 'chat.html', {'messages': messages, 'users': User.objects.exclude(username=request.user.username)})
