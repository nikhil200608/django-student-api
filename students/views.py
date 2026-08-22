from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer


# =========================
# HTML CRUD VIEWS
# =========================

@login_required
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students},
    )


@login_required
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            email=email,
            age=age,
        )

        return redirect('student_list')

    return render(request, 'students/student_create.html')


@login_required
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
        'students/student_update.html',
        {'student': student},
    )


@login_required
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('student_list')


# =========================
# TOKEN-PROTECTED API VIEWS
# =========================

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_student_api(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_student_api(request, id):
    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = StudentSerializer(
        student,
        data=request.data,
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_student_api(request, id):
    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND,
        )

    student.delete()

    return Response(
        {'message': 'Student deleted successfully'},
        status=status.HTTP_200_OK,
    )