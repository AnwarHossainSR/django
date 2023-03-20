
from django.urls import path

from challenges import views


urlpatterns = [
    path('january', views.index),
]
