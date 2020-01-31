from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm, NameForm
from django.views.generic import TemplateView

def base(request):
    return render(request, 'base.html', {'recipes': Recipe.objects.all})

def home(request):
    context = 'context'
    return render(request, 'home.html', {'context': context})

def about(request):
    context = 'context'
    return render(request, 'about.html', {'context': context})

class New_recipe(TemplateView):
    template_name = 'new_recipe.html'

    def get(self, request):
        form = RecipeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['name']
            form = RecipeForm()
            return redirect('/')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)\

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'create_profile.html', {'form': form})