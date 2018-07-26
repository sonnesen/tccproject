from django.shortcuts import render
from django.views.generic.base import View

class HomeView(View):
    template_name = 'principal/home.html'
    context = {}
    
    def get(self, request):
        return render(request, self.template_name, self.context)
