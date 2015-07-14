from rest_framework import serializers
from student.models import Student
from group.models import Group

class StudentSerializer(serializers.ModelSerializer):
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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'group_name',
            'elder',
        )
