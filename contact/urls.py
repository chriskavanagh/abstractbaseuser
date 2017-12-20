from . import views
from django.urls import path, re_path
from django.conf.urls import url, include


app_name = 'contact'
urlpatterns = [

    #url(r'^$', views.message, name='contact'),
    path('', views.message, name='contact'),
    #url(r'^message/(?P<pk>\d+)/$', views.contact_message, name='contact_message'),
    path('message/<int:pk>/', views.contact_message, name='contact_message'),
    
]