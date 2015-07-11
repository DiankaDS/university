from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from student.models import Student


class StudentsListView(ListView):
    model = Student
    template_name = "students_list.html"


class StudentsInfoView(DetailView):
    model = Student
    template_name = "students_info.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "create_student.html"

    def get_success_url(self):
        return reverse("students:students")


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "update_student.html"

    def get_success_url(self):
        return reverse("students:students")
