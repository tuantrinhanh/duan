from django.contrib import admin
from django.urls import path
from nhanvien import views
urlpatterns = [
    path('', views.nhanvien),
    path('them_nhan_vien/', views.them_nhan_vien, name="them_nhan_vien"),
]