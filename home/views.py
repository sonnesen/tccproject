from django.shortcuts import render
from django.views.generic.base import View

class HomeView(View):
    template_name = 'home/index.html'
    context = {}
    
    def get(self, request):
        return render(request, self.template_name, self.context)
