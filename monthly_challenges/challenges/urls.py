from challenges import views
from django.urls import path

urlpatterns = [
    path("<str:month>", views.monthly_challenge),
    path("<int:month>", views.monthly_challenge_by_month),
]
