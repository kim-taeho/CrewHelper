from django.urls import path
from . import models
from . import views

app_name = "apply"

urlpatterns = [
    path("apply/<int:project_pk>/", views.create, name="create"),
]
