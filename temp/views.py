from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'temp/home.html')

def about(request):
    return render(request, 'temp/about.html')

def student_entry(request):
    return render(request, 'temp/student_entry.html')

def student_list(request):
    return render(request, 'temp/student_list.html')
