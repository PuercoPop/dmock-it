# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from dmockit import views

urlpatterns = patterns('',
        url(r'^(?P<url>.*)$',
            views.generic_view,
        ),
    )
