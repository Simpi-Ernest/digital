from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "first name"}))
    # second_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "second name"}))
    username = forms.CharField()
    # email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email"}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password"}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "confirm password"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']