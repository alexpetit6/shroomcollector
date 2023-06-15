from django.forms import ModelForm
from .models import Origin

class OriginForm(ModelForm):
    class Meta:
        model = Origin
        fields = ['city', 'state', 'date', 'description']