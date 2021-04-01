from django.shortcuts import HttpResponseRedirect, render, redirect
from django.urls import reverse

from .models import Lead
from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        'leads': leads,
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)

    context = {
        'lead': lead,
    }

    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadForm()

    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lead-list')

    context = {
        'form': form,
    }

    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lead-detail', args=[pk]))

    context = {
        'lead': lead,
        'form': form,
    }

    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('lead-list')
