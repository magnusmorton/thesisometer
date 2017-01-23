from registration.forms import RegistrationForm


class NoEmailRegistrationForm(RegistrationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields.pop('email')
