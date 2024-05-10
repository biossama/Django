from django.urls import path
from .views import index
from .views import delete

urlpatterns=[
	path('', index, name='index'),
	path('delete/<int:pk>', delete, name='delete')
]
