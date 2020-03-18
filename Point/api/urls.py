from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path('userprofile/admin/', views.AdminProfileView.as_view()),
    # path('userprofile/admin/<int:pk>/', views.AdminProfileDetail.as_view()),
    # path('userprofile/', views.UserProfileView.as_view()),
    # path('user-status/', views.UserStatusView.as_view()),
    path('infected/data/', views.InfectedView.as_view()),
    path('infected/data/<int:pk>/', views.InfectedDetailView.as_view()),
    path('transport/data/', views.TransportView.as_view()),
    path('transport/data/<int:pk>/', views.TransportDetailView.as_view()),
]
