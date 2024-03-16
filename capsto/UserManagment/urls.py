from django.urls import path,include
from . import views
#from .views import login_as_student,login_as_admin,home

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    #path('profile/', views.profile, name='profile'),
    path('studentdashboard/',include('BookManagment.urls')),
    path('admindashboard/',include('BookManagment.urls')),
    path('borrow/',include('BookManagment.urls')),
    path('login/student/', views.login_as_student, name='login_as_student'),
    path('login/admin/', views.login_as_admin, name='login_as_admin'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    
    

]


