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
    path('view/lohit', views.LohitView, name='lohit-view'),
    path('view/brahmaputra', views.BrahmaView, name='brahmaputra-view'),
    path('view/siang', views.SiangView, name='siang-view'),
    path('view/manas', views.ManasView, name='manas-view'),
    path('view/disang', views.DisangView, name='disang-view'),
    path('view/kameng', views.KamengView, name='kameng-view'),
    path('view/umiam', views.UmiamView, name='umiam-view'),
    path('view/barak', views.BarakView, name='barak-view'),
    path('view/kapili', views.KapiliView, name='kapili-view'),
    path('view/dihing', views.DihingView, name='dihing-view'),
    path('view/subansiri', views.SubanView, name='subansiri-view'),
    path('view/dhansiri', views.DhanView, name='dhansiri-view'),
    path('view/msh', views.MSHView, name='msh-view'),
    url(r'^view/(?P<slug>[\w-]+)/$', views.HABDetail, name='hab_detail'),
]
