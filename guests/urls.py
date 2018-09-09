from django.conf.urls import url, include
from django.contrib import admin

from guests import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rsvp/$', views.rsvp, name='rsvp')
    # url(r'^invite/(?P<invite_id>[\w-]+)/$', views.invitation, name='invitation')
    ]