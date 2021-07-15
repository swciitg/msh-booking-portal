from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('msh/add/', views.MSHCreate),
    path('msh/thanks/', views.MSHThanks),
]