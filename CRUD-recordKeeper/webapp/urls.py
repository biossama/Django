from django.urls import path
from . import views

app_name="webapp"

urlpatterns =[

    path('', views.home, name="home-link"),

    path('register/', views.register, name="register-link"),

    path('login/', views.login_view, name="login-link"),

    path('logout/', views.logout_view, name="logout-link"),

    path('dashboard/', views.dashboard_view, name="dashboard-link"),

    path('create/', views.create_view, name="create-link"),

    path('update/<int:pk>/', views.update_view, name="update-link"),

    path('record/<int:pk>/', views.record_view, name="record-link"),

    path('delete/<int:pk>/', views.delete_view, name="delete-link"),


]
