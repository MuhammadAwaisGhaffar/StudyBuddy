from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,  name='Login'),
    path('logout/',views.logoutPage,  name='Logout'),
    path('register/',views.registerPage,  name='Register'),
    path('',views.home, name = 'Home'),
    path('room/<str:pk>/',views.room, name='Room'),
    path('profile/<str:pk>/',views.userProfile,name='user_profile'),
    path('createRoom/', views.createRoom, name='Create_Room' ),
    path('updateRoom/<str:pk>/', views.updateRoom, name='Update_Room' ),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name='Delete_Room' ),
    path('deleteMessage/<str:pk>/', views.deleteMessage, name='delete_message' ),
    path('update-user/', views.updateUser, name='Update_User' ),
    path('topics/', views.topicsPage, name='Topics' ),
    path('activity/', views.activityPage, name='Activity' ),
]