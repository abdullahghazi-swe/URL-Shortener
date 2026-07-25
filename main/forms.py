from django import forms
from . models import UrlList

class UrlForm(forms.ModelForm):
    shorten = forms.CharField(
        required=False,
        max_length=20,
        min_length=6,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter Custom aliases",
            "class": "alias-field",
        })
    )

    class Meta:
        model = UrlList
        fields = ['input_url', 'shorten']

        widgets = {
            "input_url" : forms.URLInput(attrs={
                "placeholder": "Enter link here",
                "class": "url-field",
            })
        }

class UnshortForm(forms.Form):
    url = forms.URLField(
        widget = forms.URLInput(attrs={
            "placeholder": "Enter link here",
            "class": "url-field",
        }),
    )

