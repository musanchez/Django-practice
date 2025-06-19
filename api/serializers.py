from rest_framework import serializers
from students.models import Student
from employees.models import Employee  # Assuming you have an Employee model similar to Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # or specify fields like ('id', 'name', 'class_name') if you want to limit the fields


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # Assuming you have an Employee model similar to Student
        fields = '__all__'  # or specify fields like ('employee_id', 'employee_name', 'designation') if you want to limit the fields