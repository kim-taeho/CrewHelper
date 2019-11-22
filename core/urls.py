from django.urls import path
from projects import views as project_views

app_name = "core"

urlpatterns = [path("", project_views.HomeView.as_view(), name="home")]
