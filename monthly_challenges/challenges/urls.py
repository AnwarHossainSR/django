from challenges import views
from django.urls import path

urlpatterns = [
    path("<month>", views.monthly_challenge),
]
