from django.conf.urls import  include, url
from . import views as auth_views
from django.urls import path

urlpatterns = [
               path('', auth_views.post_list),
               path('create/', auth_views.create),
               path('some_func/', auth_views.some_func),
               path('user/', auth_views.post_listA),
               ]
