from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
	path('register/', views.register_view, name="register_link"),
	path('login/', views.login_view, name="login_link"),
	path('logout/', views.logout_view, name="logout_link"),
]
