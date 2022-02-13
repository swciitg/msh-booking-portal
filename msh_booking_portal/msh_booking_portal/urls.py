from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('campus_return/admin/', admin.site.urls),
    path('campus_return/accounts/login/',views.LoginAllAuthView.as_view(),name="home"),
    path('campus_return/accounts/', include('allauth.urls')),
    path('campus_return/logout/', LogoutView.as_view()),
    path('campus_return/', include('hab_portal.urls')),
]

urlpatterns += staticfiles_urlpatterns()
