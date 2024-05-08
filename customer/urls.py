from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('account',views.account,name='account'),
    path('signout',views.signout,name='signout'),

]