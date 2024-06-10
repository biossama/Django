from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('users/', include('users.urls')),
    path('', views.home, name=""),
    path('about/', views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

