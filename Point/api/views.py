from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from ..models import AdminUser, infection
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = AdminProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        request.data['username'] = instance.username
        serializer = AdminProfileSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserStatusView(generics.RetrieveAPIView):
    """View To Return The User Status (Active/Superuser)"""

    permission_classes = (IsAuthenticated,)
   # authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, *Args, **kwargs):
        user_instance = request.user
        data = {'is_active': user_instance.is_active,
                'is_superuser': user_instance.is_superuser}
        return Response(data, status=status.HTTP_200_OK)


class AdminProfileView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('-pk')
    serializer_class = AdminProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'first_name': ["contains"],
        # 'locaton': ["contains"]
    }


class AdminProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('-pk')
    serializer_class = AdminProfileSerializer


class ProfileData(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AdminUser.objects.all().order_by('-pk')
    serializer_class = ProfileSerializer


class InfectedView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = infection.objects.all().order_by('-pk')
    serializer_class = InfectedSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'start_hour': ["icontains"],
        'address': ["icontains"],
        'name': ["icontains"],
        'place_type': ["icontains"],
        'location': ["icontains"],
        'type': ["exact"],
        'date': ['gte', 'lte', 'exact']

        # 'locaton': ["contains"]
    }


class InfectedDetailView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = infection.objects.all().order_by('-pk')
    serializer_class = InfectedSerializer
