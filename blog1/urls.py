from django.conf.urls import  include, url
from . import views
from django.urls import path

urlpatterns = [
               url(r'^$', views.post_list),
               path('user/', views.post_listA),
               ]
