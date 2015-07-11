from django.shortcuts import render
from django.views.generic import ListView, DetailView
from group.models import Group

class GroupsListView(ListView):
    model = Group
    template_name = "groups_list.html"

class GroupsInfoView(DetailView):
    model = Group
    template_name = "groups_info.html"
