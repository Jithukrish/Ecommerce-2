from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list_products',views.list_products,name='list_products'),
    path('detail_description/<int:pk>',views.detail_description,name='detail_description'),
    path('detail_products/<int:pk>',views.detail_products,name='detail_products'),
]