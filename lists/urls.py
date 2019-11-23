from django.urls import path
from . import views


app_name = "lists"

urlpatterns = [
    path("toggle/<int:project_pk>/", views.toggle_project, name="toggle-project"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
]
