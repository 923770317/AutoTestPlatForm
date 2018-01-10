# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Systems(models.Model):
    name = models.CharField(u'系统',max_length=20)
    logic_delete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Models(models.Model):
    system = models.ForeignKey(Systems)
    name = models.CharField(u'模块', max_length=20)
    logic_delete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Request(models.Model):
    model = models.ForeignKey(Models)
    name = models.CharField(u'接口名', max_length=20,null=False,blank=False)
    protocol_type = models.CharField(u'协议类型',max_length=10,null=False,blank=False)
    method = models.CharField(u'请求方法',max_length=20,null=False,blank=False)
    url = models.CharField(u'请求地址',max_length=100,null=False,blank=False)
    headers = models.CharField(u'请求头',max_length=300,null=True,blank=True)
    request_body= models.CharField(u'请求体',max_length=500,null=True,blank=True)
    is_ci = models.BooleanField(u'是否持续集成',default=False)
    logic_delete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name