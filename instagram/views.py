from django.shortcuts import render, render

# Create your views here.

def welcome(request):
    current_user =request.user
    posts = Image.images_all()
    profile = Profile.objects.get(username=current_user)
    users = Profile.objects.all()
    to_follow = User.objects.all().exclude(id=request.user.id)
    return render(request, 'index.html', {"posts":posts,"profile":profile, "users":users, "views":to_follow}