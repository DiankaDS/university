from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from group.views import GroupsListView, GroupsInfoView, GroupUpdateView, \
    GroupDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(GroupsListView.as_view()), name="groups"),
    url(r'^(?P<pk>\d+)/$', login_required(GroupsInfoView.as_view()),
        name="info"),
    url(r'(?P<pk>\d+)/update/$', login_required(GroupUpdateView.as_view()),
        name="update"),
    url(r'(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()),
        name="delete"),
)
