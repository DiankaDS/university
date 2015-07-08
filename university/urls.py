from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home_page.html"),
        name="home_page"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': "home_page"}, name="logout"),
    url(r'^accounts/profile/', RedirectView.as_view(pattern_name="home_page")),
    url(r'^admin/', include(admin.site.urls)),
]
