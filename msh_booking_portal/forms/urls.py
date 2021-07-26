from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.index),
    path('msh/add/', views.MSHCreate),
    path('msh/edit/', views.MSHEdit),
    url(r'msh/view/$', views.MSHView, name = "msh_list"),
    path('msh/thanks/', views.MSHThanks),
]
