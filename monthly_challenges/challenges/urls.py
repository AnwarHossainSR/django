
from django.urls import path

from challenges import views


urlpatterns = [
    path('january', views.january),
    path('february', views.february),
]
