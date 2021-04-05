from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead
from .forms import LeadForm


class LeadListView(LoginRequiredMixin, generic.ListView):
    """View for displaying leads"""
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """View for displaying one lead"""
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    """View for creating a new lead"""
    template_name = 'leads/lead_create.html'
    form_class = LeadForm
    context_object_name = 'form'

    def get_success_url(self):
        """Redirect after successful creation"""
        return reverse('leads:lead-list')

    def form_valid(self, form):
        """Sending email"""
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="rezov.n@mail.ru",
            recipient_list=["jayhosee@gmail.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    """View for updating an existing lead"""
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        """Redirect after successful update"""
        return reverse('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected lead"""
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('leads:lead-list')
