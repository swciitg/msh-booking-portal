from django.urls import path
# from .views import HABDetailView
from . import views

app_name = 'hab_portal'

urlpatterns = [
    path('view/', views.HABView, name='hab_list'),
    path('add/', views.HABCreate, name = "hab_create"),
    path('form1/', views.HAB1, name = "hab_1"),
    path('form2/', views.HAB2, name = "hab_2"),
    path('edit/', views.HABEdit, name='hab_edit'),
    path('thanks/', views.HABThanks, name='hab_thanks'),
    path('wait/', views.HABDose1Wait, name='hab_dose1wait'),
    path('download_excel/', views.Download_Excel, name='download_excel'),
    path('media/hab_portal/<path:file>', views.MediaView, name='media'),
    path('', views.index, name='hab_index'),
    path('admin-view/',views.AdminView,name='admin-view'),
    path('admin-view/mark-as-invited/', views.MarkAsInvited, name='mark-as-invited-without-id'),
    path('admin-view/mark-as-invited/<int:id>/', views.MarkAsInvited, name='mark-as-invited'),
    path('admin-view/mark-as-not-invited/', views.MarkAsNotInvited, name='mark-as-not-invited-without-id'),
    path('admin-view/mark-as-not-invited/<int:id>/', views.MarkAsNotInvited, name='mark-as-not-invited'),
    path('view/<str:hostel>/', views.HostelView, name='hostel-view'),
    path('view/<str:hostel>/approved/', views.HostelApproved, name='hostel-approved'),
    path('view/<str:hostel>/pending/', views.HostelPending, name='hostel-pending'),
    path('view/<str:hostel>/rejected/', views.HostelRejected, name='hostel-rejected'),
    path('view/accept/<str:hostel>/<int:id>/', views.HostelStatusAccept, name='hostel-status-accept'),
    path('view/decline/<str:hostel>/<int:id>/', views.HostelStatusDecline, name='hostel-status-decline'),
]
