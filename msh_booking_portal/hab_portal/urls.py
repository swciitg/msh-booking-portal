from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'hab_portal'

urlpatterns = [
    url(r'^view/$', views.HABView, name='hab_list'),
    path('add/', views.HABCreate),
    path('edit/', views.HABEdit),
    path('thanks/', views.HABThanks),
    path('', views.index),
    url(r'^view/(?P<slug>[\w-]+)/$', views.HABDetail, name='hab_detail'),
]
