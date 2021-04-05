from django.views.generic import TemplateView, CreateView
from django.urls import reverse

from .forms import CustomUserCreationForm


class LandingPageView(TemplateView):
    """View for start page"""
    template_name = 'landing.html'


class SignUpView(CreateView):
    """View for sign-up new users"""
    template_name = 'registration/sign-up.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        """Redirect after successful sign-up"""
        return reverse('login')
