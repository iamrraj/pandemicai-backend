from rest_framework import serializers
from ..models import CoronaAge, CoronaSex, CoronaComorbidity, Area, Hackathon
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
    class Meta:
        model = CoronaComorbidity
        exclude = ['id']


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = ['id']


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        exclude = ['id']
