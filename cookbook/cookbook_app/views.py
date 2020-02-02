from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm
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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['name']
            form = RecipeForm()
            return redirect('/')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)