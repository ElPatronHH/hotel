from django.contrib import admin
from .models import TipoHabitacion, Habitacion, Huesped, TipoPago, Reserva

admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(TipoPago)
admin.site.register(Reserva)
