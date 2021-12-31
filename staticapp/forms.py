from django import forms
from staticapp.models import table

class InputForm(forms.ModelForm):
    class Meta:
        model = table
        fields = '__all__'
