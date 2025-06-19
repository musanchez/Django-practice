from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.students_view),
    path('student/<str:pk>/', views.student_detail_view),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),  # Assuming you want to handle employee details similarly
]