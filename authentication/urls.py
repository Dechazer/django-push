from django.contrib import admin
from django.urls import path, include
from .import views
from django.urls import path
from .views import admin

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name= 'signup'), 
   path('signin', views.signin, name= 'signin'),
   path('signout', views.signout, name= 'signout'),
   path('admin', views.admin, name='admin')
]