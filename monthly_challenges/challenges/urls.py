from challenges import views
from django.urls import path

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_month),
    path("<str:month>", views.monthly_challenge)
]
