from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),

path('api/students/', views.create_student_api, name='create_student_api'),
path('api/students/<int:id>/', views.update_student_api, name='update_student_api'),
path('api/students/<int:id>/delete/', views.delete_student_api, name='delete_student_api'),
]