from django.shortcuts import render
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request=request, template_name='users/login.html', context=context)


def registration(request):
    if request.method == 'post':
        form = UserRegistrationForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request=request, template_name='users/registration.html', context=context)

