import logging
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from agents.mixins import OrganisorAndLoginRequiredMixin
from .models import Lead
from .forms import LeadForm, AssignLeadForm


logger = logging.getLogger(__name__)


class LeadListView(LoginRequiredMixin, generic.ListView):
    """View for displaying leads"""
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """View for displaying a lead"""
    model = Lead
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    """View for creating a new lead"""
    model = Lead
    template_name = 'leads/lead_create.html'
    form_class = LeadForm
    
    def get_form_kwargs(self, **kwargs):
        """Return the keyword arguments for instantiating the form"""
        kwargs = super(LeadCreateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
    
    def form_valid(self, form):
        """Added organisation for a lead after creating"""
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        """Sending email"""
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="rezov.n@mail.ru",
            recipient_list=["jayhosee@gmail.com"],
        )
        messages.success(self.request, "You have successfully created a lead!")
        return super(LeadCreateView, self).form_valid(form)
    
    def get_success_url(self):
        """Redirect after successful creation"""
        return reverse('leads:lead-list')


class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    """View for updating an existing lead"""
    model = Lead
    template_name = 'leads/lead_update.html'
    context_object_name = 'lead'
    form_class = LeadForm

    def get_form_kwargs(self, **kwargs):
        """Return the keyword arguments for instantiating the form"""
        kwargs = super(LeadUpdateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        """Redirect after successful update"""
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected lead"""
    model = Lead
    template_name = 'leads/lead_delete.html'
    context_object_name = 'lead'

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('leads:lead-list')


class AssignLeadView(OrganisorAndLoginRequiredMixin, generic.FormView):
    """Assign lead with an agent"""
    model = Lead
    template_name = "leads/lead_assign.html"
    form_class = AssignLeadForm

    def get_form_kwargs(self, **kwargs):
        """Return the keyword arguments for instantiating the form"""
        kwargs = super(AssignLeadView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
        
    def get_success_url(self):
        """Redirect after successful assigning"""
        return reverse("leads:lead-list")

    def form_valid(self, form):
        """Save assign lead-agent in db"""
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignLeadView, self).form_valid(form)
