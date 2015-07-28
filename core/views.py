from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView
from core.forms import RegistrationForm
from core.models import UserProfile


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("success_reg")


class UserProfileView(ListView):
    model = UserProfile
    template_name = "user_profile.html"
