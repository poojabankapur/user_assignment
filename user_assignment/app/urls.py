from django.urls import path, include
from rest_framework import routers

from app import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    path('user-list/', views.UserList, name='user-list'),
    path('user-detail/<int:pk>', views.UserDetail, name='user-detail'),
    path('user-create/', views.UserCreate, name='user-create'),
    path('user-update/<int:pk>', views.UserUpdate, name='user-update'),
    path('user-delete/<int:pk>', views.UserDelete, name='user-delete'),
]