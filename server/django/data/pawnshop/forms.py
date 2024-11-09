from typing import *
from django import forms
from django.views.generic import CreateView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from .models import PDF, Product


      
class DeleteProduct(forms.Form):
    pk = forms.IntegerField(label="Введите ID товара")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        
    def is_valid(self):
        res = super().is_valid()
        data = self.cleaned_data["pk"]
        if Product.objects.filter(pk=data).exists():
            return res and True
        self.add_error(None, f"Товара с ID = {data} не существует")
        return False
        
        
class CreatePDF(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('file', )
        labels = {"file": "Выберите файл"}
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    file_accept = ['.pdf']
    
       
    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            ext = "." + file.content_type.split('/')[1]
            if ext not in self.file_accept:
                raise ValidationError("Файл должен иметь тип .pdf")
        return file
    
    def save(self, commit = ...):
        pdf = super().save(commit=False)
        file = self.cleaned_data['file']
        pdf.name = file._name
        pdf.size = file.size
        return super().save(commit)
   
    
class DeletePDF(forms.Form):
    pk = forms.IntegerField(label="Введите ID файла")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        
    def is_valid(self):
        res = super().is_valid()
        data = self.cleaned_data["pk"]
        if PDF.objects.filter(pk=data).exists():
            return res and True
        self.add_error(None, f"Файла с ID = {data} не существует")
        return False
    
    def delete(self):
        obj = PDF.objects.get(pk=self.cleaned_data['pk'])
        obj.delete()
    
  