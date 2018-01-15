# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import JsonResponse
from models import *
import requests


from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
    models = Models.objects.all()
    return render_to_response('index.html',locals())


def sendRequest(request):
    if str(request.method) == "POST":
        status_cone = '000'
        message =''
        try:
            protocol_type = request.POST.get('protocol_type')
            method = request.POST.get('method')
            url = request.POST.get('url')
            headers = request.POST.get('headers')
            request_body = request.POST.get('request_body')
            is_ci = request.POST.get('is_ci')
            model_id = request.POST.get('model')
            response = None
            if method  == 'GET':
                if headers:
                    response = requests.get(protocol_type + '://' + url,headers = eval(headers))
                else:
                    response = requests.get(protocol_type + '://' + url)
                message = response.text
            else:
                pass

        except Exception as e:
            status_cone = '999'
            message = e.message
        return JsonResponse({'status':status_cone,'message':message})

        Request.objects.create(model_id=model_id,name='demo1',protocol_type = protocol_type,method=method,headers=headers,
                              url = url,request_body=request_body,is_ci=is_ci)
        print '111'

def saveRequest(request):
    if str(request.method) == 'POST':
        protocol_type = request.POST.get('protocol_type')
        method = request.POST.get('method')
        url = request.POST.get('url')
        headers = request.POST.get('headers')
        request_body = request.POST.get('request_body')
        is_ci = request.POST.get('is_ci')
        model_id = request.POST.get('model')

        Request.objects.create(model_id=model_id, name='demo1', protocol_type=protocol_type, method=method,
                               headers=headers,
                               url=url, request_body=request_body, is_ci=is_ci)
        return