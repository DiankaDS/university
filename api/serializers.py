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


class ElderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'year_of_birth',
            'student_id',
        )


class GroupSerializer(serializers.ModelSerializer):
    elder = ElderSerializer()
    number_of_students = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = (
            'group_name',
            'elder',
            'number_of_students',
            'students'
        )

    def get_number_of_students(self, obj):
        return obj.student_set.count()

    def get_students(self, obj):
        return StudentSerializer(obj.student_set.all(), many=True).data
