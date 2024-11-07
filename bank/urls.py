from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register1/', views.register1, name='register1'),
    path('register2/', views.register2, name='register2'),
    path('login/', views.my_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('banking/', views.banking, name='banking'),
    path('banking/deposit/', views.deposit, name='deposit'),
    path('banking/transfer/', views.transfer, name='transfer'),
    path('banking/withdrawal/', views.withdrawal, name='withdraw'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)