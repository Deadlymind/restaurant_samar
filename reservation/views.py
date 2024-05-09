from .models import Reservation
from django.shortcuts import render
from .forms import ReserveTableForm

from .models import Reservation
from django.contrib.auth.decorators import login_required


@login_required
def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form' : reserve_form}

    return render(request , 'Reservation/reservation.html' , context)


