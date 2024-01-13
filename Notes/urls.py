from django.urls import path, inlcude
from . import views

urlspatterns = [path('', views.getRoutes, name='routes')
path('', include('api'))
]