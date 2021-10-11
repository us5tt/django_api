from rest_framework import serializers
from .models import Pars



class ParsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    usd_price = serializers.CharField()
    city = serializers.CharField()
    description = serializers.CharField()
    id = serializers.IntegerField()

