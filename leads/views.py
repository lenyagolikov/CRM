from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from agents.mixins import OrganisorAndLoginRequiredMixin
from .models import Lead
from .forms import LeadForm, AssignLeadForm


class LeadListView(LoginRequiredMixin, generic.ListView):
    """View for displaying leads"""
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        """Pass extra params to the template"""
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset,
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """View for displaying a lead"""
    template_name = 'leads/lead_detail.html'

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
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

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


class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    """View for updating an existing lead"""
    template_name = 'leads/lead_update.html'
    form_class = LeadForm

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        """Redirect after successful update"""
        return reverse('leads:lead-list')


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected lead"""
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        """Filter leads, hides foreign leads"""
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('leads:lead-list')


class AssignLeadView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_lead.html"
    form_class = AssignLeadForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignLeadView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
        
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignLeadView, self).form_valid(form)
