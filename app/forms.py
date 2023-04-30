from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime 
from .models import Profile,Appointment

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserupdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

class MakeAppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date', 'min': datetime.now().date()}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'time', }))
    class Meta:
        model = Appointment
        fields = ['name','email','contact','service','date','time']

class CustomerAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']

