from django.shortcuts import render, redirect
from vendor.forms import *
from vendor.models import *
# from models impor


def country(request):
    add = 'True'
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("country") 
    else:
        user = request.user
        try:
            country = Country.objects.filter(user=user)
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CountryForm()
    data = {'form':form,'country':country,'add':add,'pro':pro}
    return render(request, 'vendor/country.html',data)


def countryedit(request,foo):
    add = 'False'
    med = Country.objects.get(id=foo)
    if request.method == "POST":
        form = CountryForm(request.POST, instance = med)
        if form.is_valid():
            form.save()
        return redirect('country')
    else:
        user = request.user
        try:
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CountryForm(instance = med)
    data = {'form':form,'add':add,'pro':pro}
    return render(request, "vendor/country.html", data)


def countrydelete(request, foo):
    med = Country.objects.get(pk=foo)
    med.delete()
    return redirect('country')

def state(request):
    add = 'True'
    if request.method == "POST":
        form = StateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("state") 
    else:
        user = request.user
        try:
            state = State.objects.filter(user=user)
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = StateForm()
    data = {'form':form,'state':state,'add':add,'pro':pro}
    return render(request, 'vendor/state.html',data)


def stateedit(request,foo):
    add = 'False'
    med = State.objects.get(id=foo)
    if request.method == "POST":
        form = StateForm(request.POST, instance = med)
        if form.is_valid():
            form.save()
        return redirect('state')
    else:
        user = request.user
        try:
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = StateForm(instance = med)
    data = {'form':form,'add':add,'pro':pro}
    return render(request, "vendor/state.html", data)


def statedelete(request, foo):
    med = State.objects.get(pk=foo)
    med.delete()
    return redirect('state')


def city(request):
    add = 'True'
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("city") 
    else:
        user = request.user
        try:
            city = City.objects.filter(user=user)
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CityForm()
    data = {'form':form,'city':city,'add':add,'pro':pro}
    return render(request, 'vendor/city.html',data)


def cityedit(request,foo):
    add = 'False'
    med = City.objects.get(id=foo)
    if request.method == "POST":
        form = CityForm(request.POST, instance = med)
        if form.is_valid():
            form.save()
        return redirect('city')
    else:
        user = request.user
        try:
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CityForm(instance = med)
    data = {'form':form,'add':add,'pro':pro}
    return render(request, "vendor/city.html", data)


def citydelete(request, foo):
    med = City.objects.get(pk=foo)
    med.delete()
    return redirect('city')


def cartype(request):
    add = 'True'
    if request.method == "POST":
        form = CarTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("cartype") 
    else:
        user = request.user
        try:
            cartype = CarType.objects.filter(user=user)
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CarTypeForm()
    data = {'form':form,'cartype':cartype,'add':add,'pro':pro}
    return render(request, 'vendor/cartype.html',data)


def cartypeedit(request,foo):
    add = 'False'
    med = CarType.objects.get(id=foo)
    if request.method == "POST":
        form = CarTypeForm(request.POST, request.FILES, instance = med)
        if form.is_valid():
            form.save()
        return redirect('cartype')
    else:
        user = request.user
        try:
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CarTypeForm(instance = med)
    data = {'form':form,'add':add,'pro':pro}
    return render(request, "vendor/cartype.html", data)


def cartypedelete(request, foo):
    med = CarType.objects.get(pk=foo)
    med.delete()
    return redirect('cartype')


def driver(request):
    add = 'True'
    if request.method == "POST":
        form = CabForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("driver") 
    else:
        user = request.user
        try:
            cab = Cab.objects.filter(user=user)
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CabForm()
    data = {'form':form,'cab':cab,'add':add,'pro':pro}
    return render(request, 'vendor/driver.html',data)


def driveredit(request,foo):
    add = 'False'
    med = Cab.objects.get(id=foo)
    if request.method == "POST":
        form = CabForm(request.POST, instance = med)
        if form.is_valid():
            form.save()
        return redirect('driver')
    else:
        user = request.user
        try:
            pro = Profile.objects.get(user=user)
        except:
            pass
        form = CabForm(instance = med)
    data = {'form':form,'add':add,'pro':pro}
    return render(request, "vendor/driver.html", data)


def driverdelete(request, foo):
    med = Cab.objects.get(pk=foo)
    med.delete()
    return redirect('driver')


def updateProfile(request):
    user = request.user
    if request.method == "POST":
        form = Profile.objects.get(user=user)
        try:
            form.adress = request.POST['adress']
            form.profile_pic = request.FILES['profile_pic']
            form.save()
        except:
            pass
        user_form = UserUpdationForm(request.POST, instance = user)
        if user_form.is_valid:
            user_form.save()
            return redirect("profile") 
    else:
        pro = Profile.objects.get(user=user)
        user_form = UserUpdationForm(instance = user)
    data = {'pro':pro, 'user_form':user_form}
    return render(request, 'vendor/update_profile.html',data)

def dashboard(request):
    return render(request, 'vendor/dashboard.html')

def dashboard1(request):
    return render(request, 'vendor/dashboard1.html')

def dashboard_static(request):
    total_country = len(Country.objects.all().values())
    total_state = len(State.objects.all().values())
    total_city = len(City.objects.all().values())
    total_cab = len(Cab.objects.all().values())

    total_users = ['total_country', 'total_state', 'total_city', 'total_cab']
    total_users_value = [total_country, total_state, total_city, total_cab]

    context = {
        'months': total_users,
        'month_counts': total_users_value,
        'month_counts_19': total_users_value
    }
    return render(request, 'vendor/dashboard_static.html',context)
