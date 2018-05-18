from django.views.generic.base import View
from django.shortcuts import render


class DashboardView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kargs):
        return render(request, self.template_name, {})
    
