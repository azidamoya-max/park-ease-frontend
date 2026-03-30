from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import AttendanceForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'attendance/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
       form = AttendanceForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('student_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/student_form.html', {'form': form, 'action': 'Record Attendance'})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
       form = AttendanceForm(request.POST, instance=student)
    if form.is_valid():
       form.save()
       return redirect('student_list')
    else:
        form = AttendanceForm(instance=student)
    return render(request, 'attendance/student_form.html', {'form': form, 'action': 'Update Record'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
       student.delete()
       return redirect('student_list')
       return render(request, 'attendance/student_confirm_delete.html', {'student': student})