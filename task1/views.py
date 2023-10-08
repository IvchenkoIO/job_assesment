from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required
def task1(request):
    from task2.models import Reservations
    from datetime import datetime
    user_groups = request.user.groups.all()
    context={}
    for group in user_groups:
        if group.name == 'Managers':
            context['role']='Manager'
        else:
            context['role']='Default'
    #data=funcs.send_xml_request(request)
    #print(data)
    #funcs.parse_xml_data(data)
    query = request.GET.get("q")
    query_d1=request.GET.get("start_date")
    query_d2=request.GET.get("end_date")
    filter_option=request.GET.get('booking_value')
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
        print("dq")
        date=datetime.strptime(query_d1, "%Y-%m-%d").date()
        reservations=Reservations.objects.filter(
            checkin_date__gte=date
        )
    elif query_d2:
        print('dd')
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
        if filter_option:
            if filter_option=='ascending':
                reservations=Reservations.objects.all().order_by('booking_value')
            else:
                reservations = Reservations.objects.all().order_by('-booking_value')
        else:
            reservations = Reservations.objects.all()

    context['reservations']=reservations

    #return render(request, 'reservation_list.html', context)
    return render(request, 'task1.html',context)