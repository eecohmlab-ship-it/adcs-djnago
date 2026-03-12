from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import StudentForm
from .models import Student

# Create your views here.

def home(request):
    return render(request, 'temp/home.html')

def about(request):
    return render(request, 'temp/about.html')

def student_entry(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))
    else:
        form = StudentForm()
    return render(request, 'temp/student_entry.html', {
        'form': form, 'title':'Add Students'
    })

def student_list(request):
    student_data = Student.objects.all()
    return render(request, 'temp/student_list.html', {'students': student_data})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'temp/student_entry.html', {'form': form, 'title': 'Update Form'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'temp/student_confirm_delete.html', {'student': student})