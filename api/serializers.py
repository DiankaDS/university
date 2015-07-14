from rest_framework import serializers
from student.models import Student

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'year_of_birth',
            'student_id',
            'group'
        )
