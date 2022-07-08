from django.shortcuts import render, redirect
from django.views.generic import View


# Create your views here.
def home(request):

	return render(request,'index.html')

from django.contrib import messages,auth
from django.contrib.auth.models import User

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'the username already used')
				return redirect('/signup')
			elif User.objects.filter(email = email).exists():
				messages.error(request,'the email already used')
				return redirect('/signup')
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()
				return redirect('/')
		else:
			messages.error(request,"the password doesn't match")
			return redirect('/signup')

	return render(request,'signup.html')

from django.contrib.auth import login,logout

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request,user)
			return redirect('/logged')
		else:
			messages.error(request,'Incorrect username or password')
			return redirect('/login')

	return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')


def logged(request):

	return render(request,'logged.html')

