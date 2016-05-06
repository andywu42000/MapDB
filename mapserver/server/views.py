# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

from .models import Mark
# Create your views here.

def mark_download(request):
    mark_list = Mark.objects.all()
    #result = []
    marks = []
    for mark in mark_list:
        mark_dict = {
            'title': unicode(mark.title),
            'content': unicode(mark.content),
            'zip': unicode(mark.zip),
            'location': unicode(mark.location),
            'latitude': unicode(mark.latitude),
            'longitude': unicode(mark.longitude),
            'open_at': unicode(mark.open_at),
            'close_at': unicode(mark.close_at),
            'created_at': unicode(mark.created_at),
            'updated_at': unicode(mark.updated_at)}
        marks.append(mark_dict)
    #result.append({"marks": marks})
    resp = json.dumps(marks, sort_keys=True)
    print resp
    return JsonResponse(resp, safe=False)