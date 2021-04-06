from django.urls import path

from .views import (
    LeadListView, LeadDetailView, LeadCreateView,
    LeadUpdateView, LeadDeleteView, AssignLeadView,
    CategoryListView, CategoryDetailView, LeadCategoryUpdateView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>', LeadDetailView.as_view(), name='lead-detail'),
    path('create', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-lead', AssignLeadView.as_view(), name='assign-lead'),
    path('<int:pk>/category', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
]
