from django.urls import path

from .views import HomePageVies

urlpatterns = [
    path('', HomePageVies.as_view(), name='home'),
]