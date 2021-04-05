from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    """View for displaying agents"""
    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    """View for displaying an agent"""
    template_name = 'agents/agent_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    """View for creating a new agent"""
    template_name = 'agents/agent_create.html'
    form_class = AgentForm
    context_object_name = 'form'

    def get_success_url(self):
        """Redirect after successful creation"""
        return reverse('agents:agent-list')

    def form_valid(self, form):
        """Assign organisation for new agent"""
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    """View for updating an agent"""
    template_name = 'agents/agent_update.html'
    queryset = Agent.objects.all()
    form_class = AgentForm

    def get_success_url(self):
        """Redirect after successful updation"""
        return reverse('agents:agent-list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    """View for deleting the selected agent"""
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        """Redirect after successful deletion"""
        return reverse('agents:agent-list')
