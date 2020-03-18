from rest_framework import serializers
from ..models import AdminUser, infection, Transport
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class AdminProfileSerializer(serializers.ModelSerializer):

    locaton = serializers.CharField(
        source='something.location', allow_blank=True, allow_null=True)
    frequency = serializers.CharField(
        source='something.location', allow_blank=True, allow_null=True)
    latitude = serializers.DecimalField(
        max_digits=9, decimal_places=6, allow_null=True)
    longitude = serializers.DecimalField(
        max_digits=9, decimal_places=6, allow_null=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'password',
                  'locaton', 'frequency', 'latitude', 'longitude']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('something', None)
        self.update_or_create_profile(instance, profile_data)
        return super(AdminProfileSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""

        AdminUser.objects.update_or_create(user=user, defaults=profile_data)


class UserStatus(serializers.ModelSerializer):
    """DRF Serializer To Get The Status Of The User (Active/Superuser)"""

    class Meta:
        model = User
        fields = ['is_active', 'is_superuser']


class InfectedSerializer(serializers.ModelSerializer):

    class Meta:
        model = infection
        fields = "__all__"


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"
