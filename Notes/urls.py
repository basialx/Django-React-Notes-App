from django.urls import path
from .views import getRoutes

urlpatterns = [
    path('', getRoutes, name='routes'),
    # Add more patterns if needed
]
