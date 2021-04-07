from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic

from leads.models import Agent
from .forms import AgentForm
from .mixins import OrganisorAndLoginRequiredMixin


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    """View for displaying agents"""
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    """View for displaying an agent"""
    template_name = 'agents/agent_detail.html'

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    """View for creating a new agent"""
    template_name = 'agents/agent_create.html'
    form_class = AgentForm

    def form_valid(self, form):
        """Invite agent to CRM and sending email him"""
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password('allison12')
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message='You were added as an agent on CRM. Please come login to start working',
            from_email='admin@test.com',
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)

    def get_success_url(self):
        """Redirect after successful creation"""
        return reverse('agents:agent-list')


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    """View for updating an agent"""
    template_name = 'agents/agent_update.html'
    form_class = AgentForm

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        user = self.request.user
        return Agent.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        """Redirect after successful updation"""
        return reverse('agents:agent-list')


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected agent"""
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('agents:agent-list')
