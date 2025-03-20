"""
URL configuration for RawAthlean project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('training/', views.training),
    path('services/', views.services),
    path('shop/', views.shop),
    path('register/', views.register),
    path('login/', views.login),
    # path('form/', views.form),
    # path('saveform/', views.saveform),
    path('formabc/', views.formabc),
    path('dashboard/', views.dashboard),
    path('homedash/', views.homedash),
    path('membership/', views.membership),
    path('personaldash/', views.personaldash),
    path('memform/', views.memform),
    path('formmem/', views.formmem),
    path('trainingform/', views.trainingform),
    path('workout/', views.workout),
    path('diet/', views.diet),

    
    

    

]
