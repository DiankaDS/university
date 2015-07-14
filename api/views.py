from api.serializers import StudentSerializer, GroupSerializer
from student.models import Student
from group.models import Group
from rest_framework.generics import ListAPIView


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer