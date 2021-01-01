from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as user_login
from django.contrib import messages
from django.forms import modelformset_factory,inlineformset_factory,TextInput
from .models import *
from .forms import *


def profileview(request,pk):
	profile = Profile.objects.get(name=pk)
	educations = profile.education.all()
	skills = profile.skill.all()
	experiences = profile.experience.all()

	context = {
		'profile':profile,
		'educations':educations,
		'skills':skills,
		'experiences':experiences,
	}

	return render(request,'userprofile/profileview.html',context)


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
			return redirect('profile')
		else:
			messages.info(request, 'Username OR Password is incorrect')

	return render(request, 'userprofile/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			
			Profile.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username) #show success message

			return redirect('login')
	context={
		'form':form,
	}
	return render(request,'userprofile/register.html',context)

@login_required(login_url='login')
def profileSettings(request):
	profile = request.user.profile
	
	educationFormSet = inlineformset_factory(Profile, Education, fields='__all__',extra=1, can_delete=True,
		widgets={
		'start_date':TextInput(attrs={'type': 'date'}),
		'end_date':TextInput(attrs={'type': 'date'}),
		})
	profile_form = profileForm(instance=profile)

	if request.method == 'POST':
		profile_form = profileForm(request.POST, request.FILES, instance=profile)
		edu_formset = educationFormSet(request.POST, instance=profile)
		if profile_form.is_valid() and edu_formset.is_valid():
		#if edu_formset.is_valid():
			profile_form.save()
			edu_formset.save()
			messages.success(request,'Profile successfuly updated.')

			return redirect('profile')

	else:
		edu_formset = educationFormSet(instance=profile) #for inlineformset_factory
		#formset = educationFormSet(queryset=profile.education.all())

	context={
		'profile':profile,
		'profile_form':profile_form,
		'edu_formset':edu_formset
	}
	return render(request,'userprofile/profilesettings.html',context)
