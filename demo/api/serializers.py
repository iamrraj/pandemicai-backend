from rest_framework import serializers
from ..models import CoronaAge, CoronaSex, CoronaComorbidity
from django.contrib.auth.models import User


class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaAge
        exclude = ['id', 'byage']


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaSex
        exclude = ['id', 'bysex']


class CoronaComorbiditySerializer(serializers.ModelSerializer):
    byAge = AgeSerializer(read_only=True, many=True)
    bySex = SexSerializer(read_only=True, many=True)

    class Meta:
        model = CoronaSex
        exclude = ['id']
