from django import forms
from films.models import Movie, Genre


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ("created_on",)

    def clean_name(self):
        name = self.cleaned_data['name']
        if "curse" in name.lower():
            raise forms.ValidationError("You can not to use frbidden words")
        return name


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if "disco" in name.lower():
            raise forms.ValidationError("You can not to use frbidden words")
        return name
