from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from . models import KickstarterCampaign
from . serializers import KickstarterCampaignSerializer

class KickstarterCampaignList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = KickstarterCampaign.objects.all()
    serializer_class = KickstarterCampaignSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class KickstarterCampaignSingle(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = KickstarterCampaign.objects.all()
    serializer_class = KickstarterCampaignSerializer
    lookup_field='id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

