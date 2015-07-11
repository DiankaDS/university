from django.shortcuts import render
from django.views.generic import ListView
from group.models import Group

class GroupsListView(ListView):
    model = Group
    template_name = "groups_list.html"
