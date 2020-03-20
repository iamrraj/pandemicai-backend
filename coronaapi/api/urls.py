from django.urls import path, include
from . import views

# ListAPIView
urlpatterns = [
    path('cronavirues/deathrate/', views.DeathRate.as_view()),
    path('cronavirues/overview/', views.CountryArea.as_view()),
    path('cronavirues/area/', views.Country.as_view()),
]
