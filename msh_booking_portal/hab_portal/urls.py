from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.HABCreate),
    path('edit/', views.HABEdit),
    path('view/', views.HABView),
    path('thanks/', views.HABThanks),
]
