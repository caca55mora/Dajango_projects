from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Appointment

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  UserProfileUpdate, UserupdateForm,UserRegistrationForm,MakeAppointmentForm,CustomerAppointmentForm

#from django.contrib.auth.forms import AuthenticationForm, UserCreateForm
#from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request, 'service.html')

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                 username=form.cleaned_data['username'],
                 password=form.cleaned_data['password'])

            login(request, user)
            print(user.is_superuser)
            if user.is_superuser == True:
                return redirect('/admindashboard/')
            else:
                return redirect('/customerdashboard/')

            
    return render(request, 'signin.html', {'form': form})

def admindashboard(request):
    return render(request, 'admindashboard.html')

def customerdashboard(request):
    return render(request,'customerdashboard.html')


def signout(request):
    logout(request)
    return redirect('/index/')

def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/index/')
        else:
            form=UserCreateForm()
        context = {
            'form' :form,
        }

    return render(request, 'signup.html',{'form': form})    


def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Done')
            return redirect('/signin/')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)  


    
def profile_user(request):
    return render(request, 'profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserupdateForm(request.POST, instance=request.user)
        user_profile = UserProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            return redirect('/profile/')
    
    else:
        user_form = UserupdateForm(instance=request.user)
        user_profile = UserProfileUpdate(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'user_profile': user_profile
    }
    
    return render(request, 'profileupdate.html', context)

    

def MakeAppointments(request):
 
    if request.method == 'POST':
        appointment_form = MakeAppointmentForm(request.POST)

        if appointment_form.is_valid() :
            appointment_form.instance.customer=request.user
            appointment_form.save()
           
            return redirect('/customerdashboard/')
    
    else:
        appointment_form = MakeAppointmentForm()
        
    context = {
        'appointment_form': appointment_form
       
    }
    
    return render(request, 'customermakeappointment.html', context)


def ViewAppointments(request):
    appointment = Appointment.objects.filter(customer=request.user)

    context = {
        'appointment': appointment
    }
    return render(request, 'customerviewappointment.html',context)

def AdminViewAppointments(request):
    appointment = Appointment.objects.all()

    context = {
        'appointment': appointment
    }
    return render(request, 'adminviewappointment.html',context)

def all_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment_form = CustomerAppointmentForm(request.POST,instance=appointment)
        if appointment_form.is_valid():
            appointment_form.save()
            return redirect('adminviewappointments')
    
    else:
        appointment_form = CustomerAppointmentForm(instance=appointment)

    context = {
        'appointment_form': appointment_form
    }

    return render(request, 'update_status.html', context)





