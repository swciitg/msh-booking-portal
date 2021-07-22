from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hab/add/', views.HABCreate),
    path('hab/edit/', views.HABEdit),
    path('hab/view/', views.HABView),
    path('hab/thanks/', views.HABThanks),
]
