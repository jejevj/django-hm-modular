# modules/forms.py
from django import forms
from .models import Module
from django.core.exceptions import ValidationError
import re
from django.utils.text import slugify


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'url_path', 'description', 'version']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If the form is for a new object and name is present in initial data
        if not self.instance.pk:
            name = self.data.get('name') or self.initial.get('name')
            if name and not self.data.get('url_path'):
                # Slugify and prefill
                suggested_slug = slugify(name)
                self.fields['url_path'].initial = suggested_slug
    def clean_url_path(self):
        url_path = self.cleaned_data['url_path']
        if not re.fullmatch(r'[a-z0-9\-\/]+', url_path):
            raise ValidationError(
                "URL path hanya bisa huruf kecil, angka, hyphens (-), dan slashes (/)."
            )
        if url_path.startswith('/') or url_path.endswith('/'):
            raise ValidationError("URL path tidak boleh dimulai atau berakhir dengan slash (/).")
        
        return url_path
