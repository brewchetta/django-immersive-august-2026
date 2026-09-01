from django.shortcuts import render, redirect
from datetime import datetime

# functional view - (it is a function)
def home(request):
    context = { "current_time": datetime.now() }
    return render(request, 'app/home.html', context)


# class based view

from django.views.generic import TemplateView

# the TemplateView is designed to show a template and not much else
class AboutPage(TemplateView):
    # template_name is the name of the template we want to show
    template_name = 'app/about.html'
    # extra_context is basically just the context you want to pass
    extra_context = { "current_time": datetime.now() }


# View is the most generic / flexible version of a class based view
from django.views import View
from .models import GamingPC
from .forms import GamingPCForm

class GamingPCCreateView(View):

    # get will fire on a 'GET' request
    def get(self, request):
        return render(request, "app/gaming_pc_create.html", { "form": GamingPCForm() })

    # post will fire on a 'POST' request
    def post(self, request):
        form = GamingPCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "app/gaming_pc_create.html", { "form": form })