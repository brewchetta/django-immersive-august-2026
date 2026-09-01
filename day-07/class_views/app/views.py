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

class GenericFormView(View):
    template_name = 'app/generic_form.html'
    form = None
    submit_text = "Submit"
    redirect_path = 'home'

    # get will fire on a 'GET' request
    def get(self, request):
        context = { "form": self.form(), "submit_text": self.submit_text }
        return render(request, self.template_name, context)

    # post will fire on a 'POST' request
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_path)
        context = { "form": form, "submit_text": self.submit_text }
        return render(request, self.template_name, context)


from .forms import GamingPCForm
class GamingPCCreateView(GenericFormView):
    form = GamingPCForm
    submit_text = "Build New Gaming PC"
    redirect_path = 'about'


# from .forms import HeadphoneForm
# class HeadphoneCreateView(GenericFormView):
#     form = HeadphoneForm
#     template_name = "app/headphones_create.html"


from django.views.generic.edit import FormView
from .forms import HeadphoneForm

class HeadphoneCreateView(FormView):
    template_name = "app/headphones_create.html"
    form_class = HeadphoneForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)