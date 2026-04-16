from django.shortcuts import render

from .models import Guest

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest
from .forms import GuestForm


# List all guests
def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guests/guest_list.html', {'guests': guests})


# Register a new guest
def guest_create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'guests/guest_form.html', {'form': form})


# Edit an existing guest
def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guests/guest_form.html', {'form': form})


# Delete a guest
def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list')
    return render(request, 'guests/guest_confirm_delete.html', {'guest': guest})