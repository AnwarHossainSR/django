from django.urls import path

from challenges import views


urlpatterns = [
    path("<month>", views.monthly_challenge),
]
