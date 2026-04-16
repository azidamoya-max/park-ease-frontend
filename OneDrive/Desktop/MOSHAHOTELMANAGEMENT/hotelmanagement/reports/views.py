from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from guests.models import Guest
from rooms.models import Room
from payments.models import Payment


def report_view(request):
    total_guests = Guest.objects.count()
    total_rooms = Room.objects.count()
    occupied_rooms = Room.objects.filter(room_status='occupied').count()
    not_occupied_rooms = Room.objects.filter(room_status='not_occupied').count()
    total_payments = Payment.objects.count()
    total_revenue = sum([p.amount for p in Payment.objects.all()])

    context = {
        'total_guests': total_guests,
        'total_rooms': total_rooms,
        'occupied_rooms': occupied_rooms,
        'not_occupied_rooms': not_occupied_rooms,
        'total_payments': total_payments,
        'total_revenue': total_revenue,
    }
    return render(request, 'reports/report.html', context)