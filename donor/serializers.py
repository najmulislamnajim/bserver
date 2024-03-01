from rest_framework import serializers
from .models import DonorModel,DonationRequestModel

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonorModel
        fields='__all__'
        
class DonationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonationRequestModel
        fields='__all__'