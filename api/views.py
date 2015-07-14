from api.serializers import StudentsSerializer
from student.models import Student
from rest_framework.generics import ListAPIView


class StudentsListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

