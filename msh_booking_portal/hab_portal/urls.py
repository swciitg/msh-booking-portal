from django.urls import path
# from .views import HABDetailView
from . import views

app_name = 'hab_portal'

urlpatterns = [
    path('campus_return/view/', views.HABView, name='hab_list'),

    path('campus_return/add/', views.HABCreate, name = "hab_create"),
    path('campus_return/form2/', views.HAB2, name = "hab_2"),
    path('campus_return/form1/', views.HAB1, name = "hab_1"),
    path('campus_return/edit/', views.HABEdit, name='hab_edit'),
    path('campus_return/thanks/', views.HABThanks, name='hab_thanks'),
    path('campus_return/wait/', views.HABDose1Wait, name='hab_dose1wait'),
    path('campus_return/', views.index, name='hab_index'),
    # path('view/<int:pk>/', HABDetailView.as_view(), name='hab_detail'),
    path('campus_return/view/<str:hostel>/', views.HostelView, name='hostel-view'),
    path('campus_return/view/<str:hostel>/approved/', views.HostelApproved, name='hostel-approved'),
    path('campus_return/view/<str:hostel>/pending/', views.HostelPending, name='hostel-pending'),
    path('campus_return/view/<str:hostel>/rejected/', views.HostelRejected, name='hostel-rejected'),
    path('campus_return/view/<str:hostel>/<str:status>/<int:id>/', views.HostelStatusAccept, name='hostel-status-accept'),
    path('campus_return/view/<str:hostel>/<int:id>/', views.HostelStatusDecline, name='hostel-status-decline'),
]
