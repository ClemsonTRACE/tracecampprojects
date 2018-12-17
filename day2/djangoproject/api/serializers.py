from rest_framework import serializers
from . models import KickstarterCampaign

class KickstarterCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model=KickstarterCampaign
        fields='__all__'