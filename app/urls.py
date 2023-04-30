from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

## For image handeling
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path('',views.index),
    path('index/',views.index),
    path('contact/',views.contact),
    path('service/',views.service),

    
    path('signin/', views.signin, name="User Sign In"),
    path('admindashboard/',
         views.admindashboard,
         name="Admin Dashboard"),
    path('customerdashboard/',
         views.customerdashboard,
         name="customer Dashboard"),
    path('signout/', views.signout, name="User Sign Out"),
    path('signup/', views.signup, name="User sign up"),
    path('register/', views.registration, name='register'),
    path('welcome/', views.welcome, name='welcome'),
   
    path('profile/', views.profile_user, name='profile'),
    path('profileupdate/', views.profile_update, name='profile_update'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('makeappointments/', views.MakeAppointments, name='makeappointments'),
    path('viewappointments/', views.ViewAppointments, name='viewappointments'),
    path('adminviewappointment/', views.AdminViewAppointments, name='adminviewappointments'),
    path('all_appointment/<int:pk>', views.all_appointment, name='all_appointment'),



    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    

]

