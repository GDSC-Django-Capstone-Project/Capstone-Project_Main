from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserLoginForm
from .models import CustomUser

def home(request):
    return render(request, 'home.html')

def login_as_student(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None : 
                """and user.role == CustomUser.Student_Role.......
            would have added the above...but i thought if the admin and superadmin wanted to borrow book they can ....no need to register as student"""
                auth.login(request, user)
                return redirect('studentdashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    contex = {"Login_Form": form}
    return render(request, 'login_as_student.html',contex)

def login_as_admin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.role == CustomUser.Admin_Role:
                login(request, user)
                return redirect('admindashboard') # admin_dashboard.html should be created
            else:
                messages.error(request, 'Invalid username or password.')
    contex = {"Login_Form": form}
    return render(request, 'login_as_admin.html',contex)

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Welcome!')
            #return redirect('login_as_student')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

