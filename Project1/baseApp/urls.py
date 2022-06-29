from django.urls import path

from . import views

urlpatterns=[
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutUser,name='logout'),
    path('',views.home,name='home'),
    path('room/<str:id>',views.room,name='room'),
    path('createRoom/',views.createRoom,name='createRoom'),
    path('createTopic/',views.addTopics,name='addTopic'),
    path('updateRoom/<str:id>',views.updateRoom,name='updateRoom'),
    path('deleteRoom/<str:id>',views.deleteRoom,name='deleteRoom')
]