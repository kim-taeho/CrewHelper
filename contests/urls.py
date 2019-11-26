from django.urls import path
from . import views


app_name = "contests"

urlpatterns = [
    path("", views.scrape, name="contests"),
    path("all/", views.ContestView.as_view(), name="all"),
]
