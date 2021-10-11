from rest_framework import serializers
from .models import Pars


class ParsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pars
        fields = ('title', 'usd_price', 'city', 'description', 'id')


