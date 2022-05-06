from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from webinfo import views
from django.contrib.auth import views as auth_views

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

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html',
                                              success_url = '/'),
        name='change-password'
    ),

    path('signup/',
         views.SignupView.as_view(),
         name='signup_urlpattern'),

    path('home/',
         TemplateView.as_view(
             template_name='webinfo/home.html'),
         name='home_urlpattern'),

    path('admin/', admin.site.urls),

    path('', include('webinfo.urls')),

]
