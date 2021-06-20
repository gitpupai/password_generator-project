"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path('',views.home, name='this_home'), #we need to visit localhost:8000 (home function will run)
    path('randomcodesite',views.randomcode),#we need to visit localhost:8000/randomcodesite (randomcode func will run)
    path('templatestake',views.templatestake),
    path('password',views.func_password, name="password_home"),
    path('passwordGenerated',views.func_passgen, name="name_password"), #this is url name to refer name in password.html, in that case we can change the url path without affecting result
    path('passwordGenerated2',views.func_passgen2, name="name_password2"),
    path('about',views.func_about,name='about_website'),
    path('admin/', admin.site.urls),
]
