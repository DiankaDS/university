from api.serializers import StudentSerializer, GroupSerializer, \
    CreateGroupSerializer
from student.models import Student
from group.models import Group
from rest_framework.generics import ListAPIView, CreateAPIView


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentCreateAPIView(CreateAPIView):
    """
    <b><p> Test DATA </p></b>
    <pre>
        {
        "first_name": "Main",
        "last_name": "Main",
        "middle_name": "Main",
        "year_of_birth": 1999,
        "student_id": 666,
        "group": 1
        }
    </pre>
    """
    serializer_class = StudentSerializer


class GroupCreateAPIView(CreateAPIView):
    """
    <b><p> Test DATA </p></b>
    <pre>
        {
        "group_name": "Main"
            "elder": 1
        }
    </pre>
    """
    serializer_class = CreateGroupSerializer
