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
    path("all/", views.AllMarketProjectView.as_view(), name="all"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("finish/<int:pk>/", views.make_Finish, name="finish"),
    path("addMyJob/<int:user_pk>/<int:job_pk>/", views.add_myJob, name="addMyJob")
]
