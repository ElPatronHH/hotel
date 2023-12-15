from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            # Redirige a la nueva vista con el ID de la reserva recién creada
            return redirect('reserva_exitosa', reserva_id=reserva.id)
    else:
        form = ReservaForm()

    return render(request, 'formulario_reserva.html', {'form': form})

def reserva_exitosa(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'reserva_exitosa.html', {'reserva': reserva})
