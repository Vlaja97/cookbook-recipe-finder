from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    #body = forms.TextField(default='test')
    image = forms.FileField()
     
    class Meta:
        model = Recipe
        fields = ('name','body','image')

