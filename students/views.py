from django.shortcuts import render, redirect
from .models import Student


def home(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student-list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        image = request.FILES.get('image')
        if first_name and last_name and birth_date:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                image=image)
            return redirect('students:list')
    return render(request, 'students/student-create.html')

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student-detail.html', {'student': student})


