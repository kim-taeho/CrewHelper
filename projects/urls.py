from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("create/", views.CreateProjectView.as_view(), name="create"),
    path("<int:pk>/", views.ProjectDetail.as_view(), name="detail"),
    path("member/<int:pk>/", views.ProjectMemberDetail.as_view(), name="member-detail"),
    path(
        "member/<int:project_pk>/createjob/",
        views.create_job,
        name="create-job",
    ),
    path("toggle/<int:pk>/", views.toggle_market, name="toggle"),
]
