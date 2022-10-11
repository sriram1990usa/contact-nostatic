from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class Index(View):    
    def get(self, request):     
        return render(request, 'app/index.html')        

class ContactPageView(TemplateView):
    template_name = "app/contact.html"