from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.all_post, name='post_list'),
    path('newPost/', views.newPost, name='post_new'),
    path('<slug:slug>', views.post_page, name='post_slug'),
]
