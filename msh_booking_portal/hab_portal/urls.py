from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.HABView, name='all-view'),
    path('add/', views.HABCreate),
    path('edit/', views.HABEdit),
    #path('<roll_number>/', views.StudentDetail.as_view(), name='stud-detail'),
    path('thanks/', views.HABThanks),
    path('', views.index)
]
