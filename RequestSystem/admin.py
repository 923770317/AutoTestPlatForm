# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *

from django.contrib import admin

# Register your models here.
class SystemAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ModelsAdmin(admin.ModelAdmin):
    list_display = ('name','system')
    list_filter = ['system']
    search_fields = ['name']

class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'protocol_type', 'method', 'url', 'is_ci')
    list_filter = ['model']
    search_fields = ['name']


admin.site.register(Systems,SystemAdmin)
admin.site.register(Models,ModelsAdmin)
admin.site.register(Request,RequestAdmin)



