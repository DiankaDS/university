from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from student.views import StudentsListView, StudentsInfoView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(StudentsListView.as_view()), name="students"),
    url(r'^(?P<pk>\d+)/$', login_required(StudentsInfoView.as_view()),
        name="info")
)
