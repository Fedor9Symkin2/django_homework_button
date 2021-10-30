from django.urls import path

from .views import HomePageVies, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageVies.as_view(), name='home'),
]