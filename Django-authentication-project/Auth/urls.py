from django.urls import path
from .views import register_viwe,login_view,logout_view,deshboard_view

urlpatterns = [
    path("register/", register_viwe ,name="registration"),
    path("login/", login_view ,name="login"),
    path("logout/", logout_view,name="logout"),
    path("dashboard/", deshboard_view ,name="dashboard"),
]
