from django import forms
from .models import Ogrenci

class AnketForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = [
            'ogrenci_no', 'isim', 'soyisim', 
            'tekno_s1', 'tekno_s2',
            'el_s1', 'el_s2',
            'dil_s1', 'dil_s2',
            'strat_s1', 'strat_s2',
            'sanat_s1', 'sanat_s2',
            'sertifika'
        ]
        widgets = {
            'ogrenci_no': forms.TextInput(attrs={'class': 'form-control'}),
            'isim': forms.TextInput(attrs={'class': 'form-control'}),
            'soyisim': forms.TextInput(attrs={'class': 'form-control'}),
            'sertifika': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['ogrenci_no', 'isim', 'soyisim', 'sertifika']:
                self.fields[field].widget = forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'})