from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Profile
from .forms import NewPostForm, NewsProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
'''welcome view to process landing page'''
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user =request.user
    posts = Image.images_all()
    profile = Profile.objects.get(username=current_user)
    users = Profile.objects.all()
    to_follow = User.objects.all().exclude(id=request.user.id)
    return render(request, 'index.html', {"posts":posts,"profile":profile, "users":users, "views":to_follow})
