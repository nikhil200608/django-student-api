from django.shortcuts import render, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )


def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

        return redirect('student_list')

    return render(request, 'students/student_create.html')


def student_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')

        student.save()

        return redirect('student_list')

    return render(
        request,
        'student_update.html',
        {'student': student}
    )
    
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('student_list')