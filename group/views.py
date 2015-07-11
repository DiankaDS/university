from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, \
    CreateView
from group.models import Group


class GroupsListView(ListView):
    model = Group
    template_name = "groups_list.html"


class GroupsInfoView(DetailView):
    model = Group
    template_name = "groups_info.html"


class GroupUpdateView(UpdateView):
    model = Group
    template_name = "update_group.html"

    def get_success_url(self):
        return reverse("groups:groups")


class GroupDeleteView(DeleteView):
    model = Group
    template_name = "delete_group.html"

    def get_success_url(self):
        return reverse("groups:groups")


class GroupCreateView(CreateView):
    model = Group
    template_name = "create_group.html"

    def get_success_url(self):
        return reverse("groups:groups")
