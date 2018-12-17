from django.shortcuts import render
from . models import KickstarterCampaign
from django.http import HttpResponse
from django.core import serializers

def get_kickstarter(request, id):
    instance =  KickstarterCampaign.objects.filter(id = id)
    json = serializers.serialize('json', instance, fields=('backers_count','blurb'))
    return HttpResponse(json)

def get_all_kickstarter(request):
    instance =  KickstarterCampaign.objects.all()
    json = serializers.serialize('json', instance, fields=('backers_count','blurb'))
    return HttpResponse(json)