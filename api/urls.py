from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from api.views import StudentListAPIView, GroupListAPIView, \
    StudentCreateAPIView, GroupCreateAPIView

urlpatterns = [
    url(r'^students/$', login_required(StudentListAPIView.as_view()),
        name="students"),
    url(r'^groups/$', login_required(GroupListAPIView.as_view()),
        name="groups"),
    url(r'^create_student/$', StudentCreateAPIView.as_view(),
        name="create_student"),
    url(r'^create_group/$', GroupCreateAPIView.as_view(), name="create_group"),
]
