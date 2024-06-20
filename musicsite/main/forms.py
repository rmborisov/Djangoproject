from .models import MusicTask
from django.forms import ModelForm, TextInput

class MusicTaskForm(ModelForm):
    class Meta:
        model = MusicTask
        fields = ["title", "musictask"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "musictask": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }