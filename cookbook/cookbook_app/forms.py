from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
     
    class Meta:
        model = Recipe
        fields = ('name',)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)