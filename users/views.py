"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/21/20 - First Sprint - Added the register and profile Views

"""
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from shop.models import Book

"""

register method (Created on 1/21/20) -  This is a function-based view for the user registration. It takes
in the request and renders the registration template. 

"""

def register(request):
	if request.method == 'POST' :
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,'Account Successfully Created')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

"""

profile method (Created on 1/21/20) -  This is a function-based view for the user's profiles. It takes
in the request and renders the user's profile template. 

"""

@login_required
def profile(request):
	user = request.user
	books = Book.objects.filter(seller=request.user).order_by('-timestamp')
	if request.method == 'POST' :
		update_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if update_form.is_valid() and profile_form.is_valid():
			update_form.save()
			profile_form.save()
			messages.success(request,'Account Information Successfully Updated')
			return redirect('profile')
	else:
		update_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'update_form': update_form,
		'profile_form': profile_form,
		'books' : books
	}
	return render(request,'users/profile.html', context)
