from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            # new_user = authenticate(username=form.cleaned_data['email'],
            #                         password=form.cleaned_data['password1']
            #                         )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'Registration/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm()
#         if form.is_valid():
#             login(request, form.get_data('username'))
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'Registration/login.html', {'form': form})
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#
#     if request.method == 'POST':
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#
#         try:
#             user = User.objects.get(email=email)
#         except:
#             messages.warning(request,f"User with {email} does not exist")
#
#
#         user = authenticate(request, email = email, password = password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You are logged in ')
#             return redirect("home")
#         else:
#             messages.warning(request, 'User des not exist, create an account ')
#     return render(request, 'Registration/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'Registration/logout.html')