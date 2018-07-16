from django.views.generic.base import View
from django.shortcuts import render


class DashboardView(View):
    template_name = 'dashboard/index.html'
    context = {}
    
    def get(self, request):
        return render(request, self.template_name, self.context)
    
