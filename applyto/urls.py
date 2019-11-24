from django.urls import path
from . import models
from . import views

app_name = "applyto"

urlpatterns = [
    path("apply/<int:project_pk>/", views.create, name="create"),
    path("delete/<int:project_pk>/", views.delete, name="delete"),
    path("<int:pk>/", views.ApplyDetailView.as_view(), name="detail"),
    path("toggle/<int:pk>/", views.toggle_applyto, name="toggle"),
]
