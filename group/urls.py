from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from group.views import GroupsListView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(GroupsListView.as_view()), name="groups"),
)

