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
