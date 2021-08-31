from django.urls import path
from .views import HABDetailView
from . import views

app_name = 'hab_portal'

urlpatterns = [
    path('view/', views.HABView, name='hab_list'),
    path('add/', views.HABCreate, name = "hab_create"),
    path('edit/', views.HABEdit, name='hab_edit'),
    path('thanks/', views.HABThanks, name='hab_thanks'),
    path('', views.index, name='hab_index'),
    path('view/<int:pk>/', HABDetailView.as_view(), name='hab_detail'),
    path('view/<str:hostel>/', views.HostelView, name='hostel-view'),
    path('view/<str:hostel>/approved/', views.HostelApproved, name='hostel-approved'),
    path('view/<str:hostel>/pending/', views.HostelPending, name='hostel-pending'),
    path('view/<str:hostel>/rejected/', views.HostelRejected, name='hostel-rejected'),
    path('view/<str:hostel>/<str:status>/<int:id>/', views.HostelStatusAccept, name='hostel-status-accept'),
    path('view/<str:hostel>/<int:id>/', views.HostelStatusDecline, name='hostel-status-decline'),
]
