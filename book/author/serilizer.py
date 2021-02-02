from rest_framework import serializers
from .models import Gateau

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'