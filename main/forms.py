from django import forms
from .models import Shaxs

class ShaxsForm(forms.ModelForm):
    class Meta:
        model = Shaxs
        fields = ['Ismi', 'Familyasi', 'Sharfi', 'viloyat', 'tuman', 'maktab', 'maxallasi', 'JSHSHIR', 'Telefon_raqam', 'Biladigan_tili','Til_bilish_darajasi','Holati']
