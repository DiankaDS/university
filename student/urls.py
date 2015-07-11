from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from student.views import StudentsListView, StudentsInfoView, StudentCreateView, \
    StudentUpdateView, StudentDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(StudentsListView.as_view()), name="students"),
    url(r'^(?P<pk>\d+)/$', login_required(StudentsInfoView.as_view()),
        name="info"),
    url(r'create_student/$', login_required(StudentCreateView.as_view()),
        name="create"),
    url(r'^(?P<pk>\d+)/update/$', login_required(StudentUpdateView.as_view()),
        name="update"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(StudentDeleteView.as_view()),
        name="delete"),
)
