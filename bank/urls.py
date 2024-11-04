from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register1/', views.register1, name='register1'),
    path('register2/', views.register2, name='register2'),
    path('login/', views.my_login, name='login')
]
