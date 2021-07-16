from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('msh/add/', views.MSHCreate),
    path('msh/edit/', views.MSHEdit),
    path('msh/view/', views.MSHView),
    path('msh/thanks/', views.MSHThanks),
]