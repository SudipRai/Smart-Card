"""smartcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

urlpatterns = [
    path('dashboard',views.dashboard),
    path('admin',views.adminlogin),
    path('entry',views.entry),
    path('submit',views.submit),
    path('checkout',views.checkout),
    path('login',views.login),
    path('adduser',views.adduser),
    path('logindetail',views.customerlogin),
    path('home',views.home),
    path('profile',views.profile),
    path('editform/<int:id>',views.editform),
    path('save/<int:id>',views.save),
    path('profileview',views.profileview),
    path('check',views.check),
    path('profiledetail',views.profiledetail),
    path('addprofile',views.addprofile),
    path('vcard/<int:id>',views.vcard),

]

