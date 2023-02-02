from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from contractors.models import Contractor


class ContractorList(ListView):
    model = Contractor
    template_name = 'contractors/contractor_list.html'
    context_object_name = 'contractors'
    paginate_by = 10
