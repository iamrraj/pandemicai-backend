from django.urls import path, include
from . import views

# ListAPIView
urlpatterns = [
    path('cronavirues/deathrate/', views.DeathRate.as_view()),
]
