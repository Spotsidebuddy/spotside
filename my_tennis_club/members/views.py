from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import request

from .models import Member


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def all_members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

