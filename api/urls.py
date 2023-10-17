from django.urls import path
from .views import deteccion_neumonia_view

urlpatterns = [
    path('deteccion_neumonia/', deteccion_neumonia_view, name='deteccion_neumonia'),
]