from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import KickstarterCampaign
from . serializers import KickstarterCampaignSerializer

class KickstarterCampaignList(APIView):
    def get(self, request):
        KickstarterCampaigns = KickstarterCampaign.objects.all()
        serializer=KickstarterCampaignSerializer(KickstarterCampaigns, many=True)
        return Response(serializer.data)
    def post(self):
        pass
         