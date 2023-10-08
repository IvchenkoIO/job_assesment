from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.db.models import Q

def task2(request):
    from . import funcs
    from .models import Reservations
    from datetime import datetime
    #data=funcs.send_xml_request(request)
    #print(data)
    #funcs.parse_xml_data(data)
    query = request.GET.get("q")
    query_d1=request.GET.get("start_date")
    query_d2=request.GET.get("end_date")
    if query:
        reservations = Reservations.objects.filter(
            Q(quest_name__icontains=query) |
            Q(guest_email__icontains=query) |
            Q(flat_booked__icontains=query) |
            Q(checkin_date__icontains=query) |
            Q(checkout_date__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(booking_value__icontains=query)
        )
    elif query_d1:
        date=datetime.strptime(query_d1, "%Y-%m-%d").date()
        reservations=Reservations.objects.filter(
            checkin_date__gte=date
        )
    elif query_d2:
        date=datetime.strptime(query_d2, "%Y-%m-%d").date()
        reservations=Reservations.objects.filter(
            checkout_date__lte=date
        )
    elif query_d2 and query_d1:
        date1 = datetime.strptime(query_d1, "%Y-%m-%d").date()
        date2 = datetime.strptime(query_d2, "%Y-%m-%d").date()
        reservations = Reservations.objects.filter(
            checkin_date__gte=date1,
            checkout_date__lte=date2
        )
    else:
        reservations = Reservations.objects.all()

    context = {
        'reservations': reservations,
    }

    #return render(request, 'reservation_list.html', context)
    return render(request, 'task2.html',context)



# Create your views here.
