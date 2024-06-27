from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [ 
    path('', views.home , name='home'),

    path('rooms/list', views.room_list, name='room_list'),
    path('rooms/new/', views.room_new, name='room_new'),
    path('rooms/<str:room_name>/', views.room_detail, name='room_detail'),
    path('rooms/<int:room_id>/delete/', views.delete_room, name='delete_room'),

    path('login/', views.custom_login, name='custom_login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='custom_logout'),

]