from registration.backends.simple.views import RegistrationView

class GraphsRedirectView(RegistrationView):
    def get_success_url(self, user):
        return "/graphs/"
