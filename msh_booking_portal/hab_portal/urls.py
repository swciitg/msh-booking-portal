from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'hab_portal'

urlpatterns = [
    url(r'^view/$', views.HABView, name='hab_list'),
    url(r'add/$', views.HABCreate, name = "hab_create"),
    path('edit/', views.HABEdit),
    path('thanks/', views.HABThanks),
    path('', views.index),
    url(r'view/lohit/$', views.LohitView, name='lohit-view'),
    url(r'view/brahmaputra/$', views.BrahmaView, name='brahmaputra-view'),
    url(r'view/siang/$', views.SiangView, name='siang-view'),
    url(r'view/manas/$', views.ManasView, name='manas-view'),
    url(r'view/disang/$', views.DisangView, name='disang-view'),
    url(r'view/kameng/$', views.KamengView, name='kameng-view'),
    url(r'view/umiam/$', views.UmiamView, name='umiam-view'),
    url(r'view/barak/$', views.BarakView, name='barak-view'),
    url(r'view/kapili/$', views.KapiliView, name='kapili-view'),
    url(r'view/dihing/$', views.DihingView, name='dihing-view'),
    url(r'view/subansiri/$', views.SubanView, name='subansiri-view'),
    url(r'view/dhansiri/$', views.DhanView, name='dhansiri-view'),
    url(r'view/msh/$', views.MSHView, name='msh-view'),
    url(r'^view/(?P<slug>[\w-]+)/$', views.HABDetail, name='hab_detail'),
]
