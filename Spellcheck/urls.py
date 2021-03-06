"""Spellcheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^admin$', admin.site.urls),
    url(r'^$', views.main, name='Main page'),
    url(r'^main[/]{0,1}$', views.main, name='Main page'),
    url(r'^main.html[/]{0,1}$', views.main, name='Main page'),
    url(r'^index[/]{0,1}$', views.main, name='Main page'),
    url(r'^index.html[/]{0,1}$', views.main, name='Main page'),
    url(r'^login/$', views.loginInAccount, name='Log in'),
    url(r'^account/$', views.account, name='Log in'),
    url(r'^/logout$', views.logout, name='Main page'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('', include('social_django.urls', namespace='social')),
    url(r'^accounts/login/', include('django.contrib.auth.urls')),
    url(r'^deleteQuery/$', views.deleteQuery, name='Main page'),
    url(r'^checkInputedText/$', views.checkInputedText, name='Check text'),
    #url(r'^', views.notFound, name='Page not found'),
    url(r'^', views.main, name='Main page'),

]
