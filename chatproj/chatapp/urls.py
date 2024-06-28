from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [ 
    path('', views.home , name='home'),
    path('services/', views.services , name='services'), #D
    path('contact/', views.contact , name='contact'), #D
    path('pricing/', views.pricing , name='pricing'), #D

    path('rooms/list', views.room_list, name='room_list'),
    path('rooms/new/', views.room_new, name='room_new'),
    path('rooms/<str:room_name>/', views.room_detail, name='room_detail'),
    path('rooms/<int:room_id>/delete/', views.delete_room, name='delete_room'),
    path('rooms/<str:room_name>/delete/<int:message_id>/', views.delete_message, name='delete_message'),


    path('login/', views.custom_login, name='custom_login'), # D
    path('signup/', views.signup, name='signup'), # D
    path('logout/', views.custom_logout, name='custom_logout'), # D

]