from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserCreation

@login_required
def index(request):
    return render(request, 'accounts/index.html')

def sign_up(request):
    context = {}
    form = CustomUserCreation(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render (request, 'accounts/index.html')
    context['form']=form
    return render(request, 'registration/sign_up.html', context)

def settings(request):
    pass

def leaderboards(request):
    pass

def how_it_works(request):
    pass