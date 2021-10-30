from django.urls import path

from .views import Picture1, Picture2, Picture3

urlpatterns = [
    path('picture3/', Picture3.as_view(), name='picture3'),
    path('picture2/', Picture2.as_view(), name='picture2'),
    path('', Picture1.as_view(), name='picture1'),
]