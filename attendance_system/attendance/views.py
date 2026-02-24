from django.shortcuts import render, redirect
from .models import Student, Attendance
from datetime import date


def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def mark_attendance(request, student_id, status):
    student = Student.objects.get(id=student_id)

    Attendance.objects.create(
        student=student,
        date=date.today(),
        status=status
    )

    return redirect('home')

    return redirect('home')
def view_attendance(request):
    records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'records': records})