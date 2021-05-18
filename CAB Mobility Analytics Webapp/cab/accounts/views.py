from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm, CabPredictionForm, ContactUs
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import *
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from vendor.models import Profile
from vendor.forms import UserUpdationForm
from model import model


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            profile = Profile()
            profile.user = user
            profile.save()
            form = Profile.objects.get(user=user)
            form.profile_pic = "uploads/cars/logo_profile.jpg"
            form.save()
            messages.success(request,f'Hi, {username}  Your account created successfully')
            return redirect("login")  
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    context = {'form':form,'profile_form':profile_form}
    return render(request,'accounts/register.html', context)


def profile(request):
    user = request.user
    acc = CreateUser.objects.get(user=user)
    acc_user = acc.user_acc
    acc_user = str(acc_user)
    if acc_user == 'Vendor':
        try:
            pro = Profile.objects.get(user=user)
            user_form = UserUpdationForm(instance = user)
        except:
            pass
        data = {'user':user,'pro':pro,'user_form':user_form}
        return render(request,'vendor/home_profile.html',data)
    else:
        user_creation_date = CreateUser.objects.get(user=user)
        user_creation_date = (user_creation_date.date)
        print(user_creation_date)
        m = now().month - user_creation_date.month
        customer_since_month = abs(m)
        form = CabPredictionForm()
        context = {'form':form,'customer_since_month':customer_since_month, 'customer_name': user.username}
        return render(request,'accounts/user.html', context)

def home(request):
    return render(request, 'accounts/home.html')

def contactus(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        form.save()
        context = {
            "message": "Your message is send to Authority!"
        }
        return render(request, 'accounts/contactus.html', context)
        
    return render(request, 'accounts/contactus.html')

def predict(request):
    if request.method == 'POST':
        name = request.POST["name"]
        destination_type = request.POST["destination_type"]
        customer_rating = request.POST["customer_rating"]
        trip_distance = request.POST["trip_distance"]
        gender = request.POST["gender"]
        surge_pricing_type = request.POST["surge_pricing_type"]
        life_style_index = request.POST["life_style_index"]
        cancellation_month = request.POST["cancellation_month"]
        customer_since_month = request.POST["customer_since_month"]

        
        #predicted_price = model.predict_price(100,10.0,5,4,4,19,1,3)
        predicted_price = model.predict_price(trip_distance, customer_since_month, life_style_index, destination_type,
                                         customer_rating, cancellation_month, gender, surge_pricing_type)
        print(predicted_price)

        if predicted_price == 1:
            image_path = "accounts/img/car_1.jpeg"
            car_type = "Micro"
            car_about = "Compact yet comfortable AC cars that seat up to 3 people and give you great value for the money. Small fares for short rides."

        elif predicted_price == 2:
            image_path = "accounts/img/car_2.jpeg"
            car_type = "SUV"
            car_about = "A perfect choice of car for your weekend gateways , with plenty of room for everyone including extra bag."

        elif predicted_price == 3:
            image_path = "accounts/img/car_4.jpeg"
            car_type = "Prime Sedan"
            car_about = "Top rated drivers , and a hand-picked fleet of the best cars with extra legroom and boot space."

        elif predicted_price == 4:
            image_path = "accounts/img/car_3.jpeg"
            car_type = "mini"
            car_about = "A regular comfortable AC hatchback that becomes your everyday dependable ride.An economical option for daily routine."

        else:
            image_path = "accounts/img/car_5.jpeg"
            car_type = "Lux"
            car_about = "Compact yet comfortable AC cars that seat up to 3 people and give you great value for the money. Small fares for short rides."

        # import pdb; pdb.set_trace()

        context = {
            'customer_name': name,
            'predicted_price': predicted_price,
            'image_path': image_path,
            'car_about': car_about,
            'car_type': car_type
        }

    return render(request, 'accounts/output.html', context)

def output(request):
    # contex
    return render(request, 'accounts/output.html')






