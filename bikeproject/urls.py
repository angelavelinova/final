"""bikeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views

from pages.views import (home_view,
	contacts_view,
	start_page_view,
	login_view,
	signup,
	profile_view,
	founders_view,
	data_view,
	about_view,
	marshrutes_view) #profile_dynamic_view
from bike.views import (bike_view_details,
	bike_creat_form)


urlpatterns = [
	path('', home_view, name='home'),
	path('contacts/', contacts_view),
	path('founders/', founders_view),
	path('about/', about_view),
	path('start_page/', start_page_view),
	path('admin/', admin.site.urls),
	path('login_page/',login_view),
	path('signup/',signup),
	path('bike_details/',bike_view_details),
	path('bike_form/',bike_creat_form),
	path('profile/', profile_view, name='profile'),
	path('marshrutes/', marshrutes_view, name='marshrutes'),
	path('data/', data_view, name='data'),
	#path('profile/<str:user>/', profile_dynamic_view, name='profile2'),  #don't need for now

]

