from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password==re_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
            # Email verification
            # subject = 'Email verification from Insta-Blog'
            # message = 'Hey there! we have got your user request. A user has been created on this email.'
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [save_it.email, settings.EMAIL_HOST_USER]
            
            # send_mail(subject, message, from_email, to_list, fail_silently=True)

        else:
            messages.error(request, f'Password does not match')
            return redirect('register')

        return redirect('login')

    else:
        return render(request, 'register.html')