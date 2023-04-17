from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from ticket_booking.models import Update_profile
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about_us(request):
    return render(request,'about_us/about_us.html')

def contact_us(request):
    return render(request,'contact/contact.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Provide correct username and password')
                return redirect('login')
    return render(request,'login/login.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            re_pass = request.POST['re-password']

            if password != re_pass:
                messages.error(request, 'Pasword does not match')
                return redirect('register')
            if len(password) < 6 :
                messages.error(request, 'Password should be grater than 5 character')
                return redirect('register')

            user = User.objects.create_user(username=username,password=password,email=email)
            user.is_active = False
            user.first_name = fname
            user.last_name = lname
            user.save()
            if User.objects.filter(username = username).first():
                # messages.error(request, "This username is already taken please login")
                return redirect('login')
            return redirect('login')

    return render(request,'register/register.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile_setting(request):
    user = request.user
    if request.method == "POST":
        new_fname = request.POST['new_fname']
        new_lname = request.POST['new_lname']
        new_email = request.POST['new_email']
        new_phone = request.POST['new_phone']
        gender = request.POST['gender']
        address = request.POST['new_address']

        user.first_name = new_fname
        user.last_name = new_lname
        user.email = new_email
        user.save()
        # new_info = Update_profile.objects.update(new_phone=new_phone, gender=gender, address=address)
        # new_info.save()

        print(user.email,user.address,user.new_phone)
        
        return redirect('success_message')
    
    return render(request, 'profile_setting/profile_setting.html')


def success_page(request):

    return render(request, 'profile_update_message/profile_update.html')