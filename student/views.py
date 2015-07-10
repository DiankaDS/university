from django.shortcuts import render
from django.views.generic import ListView, DetailView
from student.models import Student


class StudentsListView(ListView):
    model = Student
    template_name = "students_list.html"


class StudentsInfoView(DetailView):
    model = Student
    template_name = "students_info.html"
