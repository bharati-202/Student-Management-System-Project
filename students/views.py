from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.contrib import messages

def home(request):
     return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    query = request.GET.get('q')  # URL se search query fetch karo
    if query:
        students = Student.objects.filter(first_name__icontains=query)  # Search logic
    else:
        students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students, 'query': query})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

