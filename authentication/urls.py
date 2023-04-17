from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('about_us/',about_us,name='about_us'),
    path('contact_us/',contact_us,name='contact_us'),
    path('login/',user_login,name='login'),
    path('register/',user_register,name='register'),
    path('logout/',user_logout,name='logout'),
    path('profile/',profile_setting,name='profile'),
    path('success_message/',success_page, name="success_message"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "reset_password/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "reset_password_sent/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "reset/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "reset_password_complete/reset_password_complete.html"), name="password_reset_complete"),
]