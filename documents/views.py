from django.views.generic import ListView

from documents.models import Demand


class DemandList(ListView):
    model = Demand
    context_object_name = 'demands'
    template_name = 'documents/demand_list.html'
