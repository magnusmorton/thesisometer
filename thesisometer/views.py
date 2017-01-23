from registration.backends.simple.views import RegistrationView
from .forms import NoEmailRegistrationForm


class GraphsRedirectView(RegistrationView):
    form_class = NoEmailRegistrationForm

    def get_form_class(self):
        return NoEmailRegistrationForm

    def get_success_url(self, user):
        return "/graphs/"
