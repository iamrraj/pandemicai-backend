from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import generics
from . import serializers
from rest_framework import filters
from ..models import CoronaAge, CoronaComorbidity, CoronaSex
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from datetime import datetime, timedelta
# from datetime import datetime, date
# import datetime

# start = datetime.datetime.strptime(date.today(), '%Y%m%d')


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class DeathRate(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CoronaComorbidity.objects.order_by('-pk')
    serializer_class = serializers.CoronaComorbiditySerializer
