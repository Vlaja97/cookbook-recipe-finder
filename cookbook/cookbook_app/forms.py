from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    image = forms.FileField()
     
    class Meta:
        model = Recipe
        fields = ('name','image')

