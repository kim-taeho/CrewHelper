from django.urls import path
from . import models
from . import views

app_name = "notes"

urlpatterns = [
    path("create/", views.create_view, name="create"),
    path("list/", views.list_view, name="list"),
    path("<int:pk>/update/", views.update_view, name="update"),
]
