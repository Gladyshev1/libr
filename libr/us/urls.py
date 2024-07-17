from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = "us"
urlpatterns = [
    # http://127.0.0.1:8000/users/
    path("reg", views.register, name="reg"),
    path("log", LoginView.as_view(template_name='us/log.html'), name="log"),
    path("out123", LogoutView.as_view(), name="logout"),
]