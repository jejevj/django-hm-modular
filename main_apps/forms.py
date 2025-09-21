# modules/forms.py
from django import forms
from .models import Module
from django.core.exceptions import ValidationError
import re

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'url_path', 'description', 'version']
    
    def clean_url_path(self):
        url_path = self.cleaned_data['url_path']
        if not re.fullmatch(r'[a-z0-9\-\/]+', url_path):
            raise ValidationError(
                "URL path hanya bisa huruf kecil, angka, hyphens (-), dan slashes (/)."
            )
        if url_path.startswith('/') or url_path.endswith('/'):
            raise ValidationError("URL path tidak boleh dimulai atau berakhir dengan slash (/).")
        
        return url_path
