from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *
import datetime

# Create your views here.
day = datetime.datetime.now().day
year = datetime.datetime.now().year
month = datetime.datetime.now().month

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'User already Exist!!!')
                return redirect('sign-up')
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                messages.info(request, 'User Created Successfully...')
                return redirect('login')
        else:
            messages.info(request, 'Password and Comfirm Password missed match!!!')
            return redirect('sign-up')

    return render(request, 'sign-up.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if User.objects.filter(username=username).exists():
                if len(username) < 1 or len(password) < 1:
                    messages.info(request, 'Please Enter your username and password')
                    return redirect('login')
                else:
                    auth.login(request, user)
                    return redirect('/')
        else:
            messages.info(request, 'Incorrect Username or Password!!!')
            return redirect('login')

    return render(request, 'login.html')

def add_farm_details(request):
    if request.method == 'POST':
        farm_location = request.POST['farm-location']
        farm_size = request.POST['farm-size']
        if len(farm_location) < 1 or len(farm_size) < 1:
            messages.info(request, 'You did not add any thing...')
            return redirect('add-farm-details')
        else:
            new_farm_detail = FarmDetails.objects.create(farm_location=farm_location, farm_size=farm_size)
            new_farm_detail.save()
            messages.info(request, 'New Farm Detail added successfully...')
            return redirect('farm-detail-view')
    return render(request, 'farm/add-farm-details.html')

def farmer_view(request):
    data = Farmers.objects.all()
    return render(request, 'farmers/farmer-view.html', {'data':data})

def officer_view(request):
    data = Officer.objects.all()
    return render(request, 'officers/officer-view.html', {'data':data})

def visit_history(request):
    history = Visit_history.objects.all()
    return render(request, 'visit-history.html', {'history':history})

def asign_form(request, id):
    farmer = Farmers.objects.get(id=id)
    farms = FarmDetails.objects.all()
    if request.method == 'POST':
        farm = request.POST['farm']
        farmer.farm = farm
        farmer.save()
        messages.info(request, 'Farm Asigned Successfully...')
        return redirect('farmer-view')
    return render(request, 'asign-farm.html', {'farms':farms, 'farmer':farmer})

def asign_form2(request, id):
    farmer = Officer.objects.get(id=id)
    farms = FarmDetails.objects.all()
    if request.method == 'POST':
        farm = request.POST['farm']
        farmer.farm = farm
        farmer.save()
        messages.info(request, 'Farm Asigned Successfully...')
        return redirect('officer-view')
    return render(request, 'asign-farm.html', {'farms':farms, 'farmer':farmer})
    
def add_officer_farmer(request):
    if request.method == 'POST':
        full_name = request.POST['full-name']
        phone_number = request.POST['phone-number']
        contact_address = request.POST['contact-address']
        extention = request.POST['extention']
        # date_visit = f"{day}/{month}/{year}"
        if len(extention) < 1:
            messages.info(request, 'Please you need to select your part!!')
            return redirect('add-officer-farmer')
        elif extention == 'Farmer':
            new_farmer = Farmers.objects.create(
                full_name=full_name, phone_number=phone_number, contact_address=contact_address,
                extention=extention
            )
            new_farmer.save()
            messages.info(request, 'Farmer Added Successfully...')
            return redirect('add-officer-farmer')
        else:
            new_officer = Officer.objects.create(
                full_name=full_name, phone_number=phone_number, contact_address=contact_address,
                extention=extention
            )
            new_officer.save()
            messages.info(request, 'Officer Added Successfully...')
            return redirect('add-officer-farmer')
    return render(request, 'add-officer-farmer.html')

def farm_detail_view(request):
    f_details = FarmDetails.objects.all()
    return render(request, 'farm/farm-detail-view.html', {'f_details':f_details})

def farm_update(request, id):
    data = FarmDetails.objects.get(id=id)
    return render(request, 'farm/farm-update.html', {'data':data})

def user_update(request, id):
    data = User.objects.get(id=id)
    return render(request, 'user-update.html', {'data':data})

def update_user(request, id):
    data = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        data.username = username
        data.email = email
        data.save()
        messages.info(request, 'User Updated Successfully...')
        return redirect('users')

def update_farm(request, id):
    data = FarmDetails.objects.get(id=id)
    if request.method == 'POST':
        farm_location = request.POST['farm-location']
        farm_size = request.POST['farm-size']

        data.farm_location = farm_location
        data.farm_size = farm_size
        data.save()
        messages.info(request, 'Farm Data Updated Successfully...')
        return redirect('farm-detail-view')

def request_for_delete(request, id):
    data = FarmDetails.objects.get(id=id)
    return render(request, 'request-for-delete.html', {'data':data})

def delete(request, id):
    data = FarmDetails.objects.get(id=id)
    data.delete()
    messages.info(request, 'Data Deleted Successfully....')
    return redirect('farm-detail-view')

def request_for_delete2(request, id):
    data = Farmers.objects.get(id=id)
    return render(request, 'farmers/request-for-delete2.html', {'data':data})

def delete2(request, id):
    data = Farmers.objects.get(id=id)
    data.delete()
    messages.info(request, 'Data Deleted Successfully....')
    return redirect('farmer-view')

def request_for_delete3(request, id):
    data = Officer.objects.get(id=id)
    return render(request, 'officers/request-for-delete3.html', {'data':data})

def delete3(request, id):
    data = Officer.objects.get(id=id)
    data.delete()
    messages.info(request, 'Data Deleted Successfully....')
    return redirect('officer-view')

def add_visit(request, id):
    data = Farmers.objects.get(id=id)
    date_visit = f"{day}/{month}/{year}"
    data.date_visit = date_visit
    data.save()
    new_visit_history = Visit_history.objects.create(full_name=data.full_name, date_visit=date_visit)
    new_visit_history.save()
    messages.info(request, 'Visit updated successfully...')
    return redirect('farmer-view')

def add_visit2(request, id):
    data = Officer.objects.get(id=id)
    date_visit = f"{day}/{month}/{year}"
    data.date_visit = date_visit
    data.save()
    new_visit_history = Visit_history.objects.create(full_name=data.full_name, date_visit=date_visit)
    new_visit_history.save()
    messages.info(request, 'Visit updated successfully...')
    return redirect('officer-view')
