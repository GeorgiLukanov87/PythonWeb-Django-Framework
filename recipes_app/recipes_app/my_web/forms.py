from django import forms

from recipes_app.my_web.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
