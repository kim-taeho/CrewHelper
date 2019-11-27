from django.urls import path
from . import views


app_name="users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("update-profile", views.UpdateProfileView.as_view(), name="update"),
    path("notifications/<int:pk>/", views.notification, name="notifications"),
    path("messages/<int:pk>/", views.user_messages, name="conversations"),

]
