from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('',
         RedirectView.as_view(
             pattern_name='home_urlpattern',
             permanent=False
         )),

    path('login/',
         LoginView.as_view(template_name='webinfo/login.html'),
         name='login_urlpattern'),

    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
    ),

    path('home/',
         TemplateView.as_view(
             template_name='webinfo/home.html'),
         name='home_urlpattern'),

    path('admin/', admin.site.urls),

    path('', include('webinfo.urls')),

]
