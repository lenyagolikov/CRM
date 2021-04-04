from django.views.generic import TemplateView, CreateView
from django.urls import reverse

from .forms import CustomUserCreationForm


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')
