from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from core.forms import RegistrationForm


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("success_reg")
