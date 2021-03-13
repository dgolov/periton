from django import forms
from .models import Applications


class ApplicationForm(forms.ModelForm):
    """ Форма обратной связи
    """
    class Meta:
        model = Applications
        fields = ('costumer_name', 'phone', 'message')
        widgets = {
            'costumer_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'message': forms.Textarea(attrs={'class': 'form-controls', 'style': 'width: 100%; height: 250px;'}),
        }
