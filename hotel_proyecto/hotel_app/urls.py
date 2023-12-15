from django.urls import path
from .views import crear_reserva, reserva_exitosa

urlpatterns = [
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('reserva_exitosa/<int:reserva_id>/', reserva_exitosa, name='reserva_exitosa'),
    # Otras URLs de tu aplicación
]
