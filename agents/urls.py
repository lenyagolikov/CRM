from django.urls import path

from .views import (
    AgentListView, AgentDetailView, AgentCreateView, AgentUpdateView, AgentDeleteView
)

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('create', AgentCreateView.as_view(), name='agent-create'),
    path('<slug:slug>', AgentDetailView.as_view(), name='agent-detail'),
    path('<slug:slug>/update', AgentUpdateView.as_view(), name='agent-update'),
    path('<slug:slug>/delete', AgentDeleteView.as_view(), name='agent-delete'),
]
