# -*- coding:utf-8 -*-

import simplejson
from os import listdir
from os.path import exists, join

from django.conf import settings
from django.http import Http404
from django.shortcuts import render


def generic_view(request, url):
    """
    """

    template = join(settings.MOCK_TEMPLATE_DIR, url)
    context = {}
    for f in listdir(settings.JSON_DIR):
        try:
            f_context = simplejson.loads(
                    ''.join(open(
                        join(settings.JSON_DIR, f),
                        'r').readlines())
                )
        except (IOError, simplejson.decoder.JSONDecodeError):
            f_context = {}
        #import ipdb; ipdb.set_trace()
        context.update(f_context)

    if exists(template):
        return render(request, template, context)
    else:
        raise Http404
