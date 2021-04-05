from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    """View for displaying agents"""
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    """View for displaying an agent"""
    template_name = 'agents/agent_detail.html'
    context_object_name = "agent"

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    """View for creating a new agent"""
    template_name = 'agents/agent_create.html'
    form_class = AgentForm

    def form_valid(self, form):
        """Assign organisation for new agent"""
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
        
    def get_success_url(self):
        """Redirect after successful creation"""
        return reverse('agents:agent-list')


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    """View for updating an agent"""
    template_name = 'agents/agent_update.html'
    form_class = AgentForm
    context_object_name = "agent"

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        """Redirect after successful updation"""
        return reverse('agents:agent-list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected agent"""
    template_name = 'agents/agent_delete.html'
    context_object_name = "agent"

    def get_queryset(self):
        """Filter agents, hides foreign agents"""
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('agents:agent-list')
