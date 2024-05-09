from django.urls import path
from .views import index
from .views import create
from .views import go

urlpatterns = [path('', index, name='index'),
               path('create', create, name = 'create'),
               path('<str:pk>', go, name = 'go'),
]
