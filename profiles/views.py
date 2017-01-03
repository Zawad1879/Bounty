from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    template = 'profiles/home.html'
    return render(request,template,context)

def about(request):
    context = {}
    template = 'profiles/about.html'
    return render(request,template,context)

@login_required
def userProfiles(request):
    user = request.user
    context = {'user': user}
    template = 'profiles/profile.html'
    return render(request,template,context)
