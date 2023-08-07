from django.urls import path
from . import views

urlpatterns = [

    path('', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('home/', views.home, name='home'),

]
