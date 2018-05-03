"""
Definition of urls for DjangoWebProject1.
"""
from django.conf.urls import url
from app.views import HomeView
from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', HomeView.as_view(),name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
