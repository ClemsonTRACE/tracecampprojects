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
        serializer = KickstarterCampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KickstarterCampaignSingle(APIView):
    def get_object(self, kick_id):
        try:
            return KickstarterCampaign.objects.get(id=kick_id)
        except KickstarterCampaign.DoesNotExist:
            raise Http404

    def get(self, request, kick_id, format=None):
        campaign = self.get_object(kick_id)
        serializer = KickstarterCampaignSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, kick_id, format=None):
        campaign = self.get_object(kick_id)
        serializer = KickstarterCampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, kick_id, format=None):
        campaign = self.get_object(kick_id)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         