from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as user_login
from django.contrib import messages
from .models import *

@login_required(login_url='login')
def profile(request):
	profile = request.user.profile
	educations = profile.education.all()
	skills = profile.skill.all()
	experiences = profile.experience.all()

	context = {
		'profile':profile,
		'educations':educations,
		'skills':skills,
		'experiences':experiences,
	}

	return render(request,'userprofile/home.html',context)

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			user_login(request,user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR Password is incorrect')

	return render(request, 'userprofile/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')
