from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva, Habitacion

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Guarda la reserva pero no cometas los cambios en la base de datos aún
            reserva = form.save(commit=False)
            
            # Busca una habitación disponible
            habitacion_disponible = Habitacion.objects.filter(
                tipo=reserva.tipo_habitacion, ocupada=False).first()

            if habitacion_disponible:
                reserva.habitacion = habitacion_disponible
                reserva.save()  # Ahora sí, guarda todo en la base de datos
                
                # Marca la habitación como ocupada
                habitacion_disponible.ocupada = True
                habitacion_disponible.save()

                return redirect('reserva_exitosa', reserva_id=reserva.id)
            else:
                # Manejar el caso en que no hay habitaciones disponibles
                pass
    else:
        form = ReservaForm()

    return render(request, 'formulario_reserva.html', {'form': form})

def reserva_exitosa(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'reserva_exitosa.html', {'reserva': reserva})
