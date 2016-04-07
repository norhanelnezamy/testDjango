from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_create,
	post_update,
	post_delete,
	post_details,
	)

urlpatterns = [
	url(r'^$', post_list),
    url(r'^create/$',post_create ),
    url(r'^details/(?P<id>\d+)/$',post_details ),
    url(r'^(?P<id>\d+)/update/$',post_update ),
    url(r'^(?P<id>\d+)/delete/$',post_delete ),
]