from . import views
from django.urls import path, re_path
from django.conf.urls import url, include



urlpatterns = [

	path('register/', views.register, name='register'),	
	path('verify/<uidb64>/<token>/',views.verify, name='verify'),
    
]