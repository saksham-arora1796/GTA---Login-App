#Saksham Arora
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(requests):
	context = {}
	template = 'home.html'
	return render(requests,template,context)

def about(requests):
	context = {}
	template = 'about.html'
	return render(requests,template,context)

@login_required
def userProfile(requests):
	user = requests.user
	context = {'user' : user}
	template = 'profile.html'
	return render(requests,template,context)