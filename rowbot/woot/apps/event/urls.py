# woot.apps.event.urls

# django
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('event.views',
       # (r'^example_url/', 'example_view')
)
