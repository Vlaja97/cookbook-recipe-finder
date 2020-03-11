from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm
from django.views.generic import TemplateView
from django.db.models import Q
import re


def base(request):
    context = {}
    # Search bar functionality
    query = request.GET.get("q", None)
    recipes = Recipe.objects.all()
    if query is not None:
        recipes = recipes.filter(Q(body__icontains=query) |
                                 Q(name__icontains=query))
    context['recipes'] = recipes
    return render(request, 'base.html', context)


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

