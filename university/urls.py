from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from core.views import UserRegistrationView, UserProfileView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home_page.html"),
        name="home_page"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': "home_page"}, name="logout"),
    url(r'^accounts/profile/', RedirectView.as_view(pattern_name="home_page")),
    url(r'^registration/$', UserRegistrationView.as_view(), name="reg"),
    url(r'^complete_registration/$', TemplateView.as_view(
        template_name="registration/success_registration.html"),
        name="success_reg"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('student.urls', namespace='students')),
    url(r'^groups/', include('group.urls', namespace='groups')),
    url(r'user_profile/$', UserProfileView.as_view(), name='user_profile'),
    url(r'api/v1/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
