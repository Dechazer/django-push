from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import signup


urlpatterns = [
   path('', views.home, name="home"),
   path('signup/', views.signup, name= 'signup'), 
   path('signin/', views.signin, name= 'signin'),
   path('signout', views.signout, name= 'signout'),
   path('admilogin/', views.admilogin, name ='admilogin')
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)