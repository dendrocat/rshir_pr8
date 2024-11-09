from typing import *
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from django.shortcuts import redirect, render, Http404, get_object_or_404
from rest_framework import generics

from .forms import *
from .models import *
from .factories import populate_cities
from .charts import generate_charts
from .serializers import *
from testsite.mixins import *



# Create your views here.
class ProductList(DataMixin, ListView):
    model = Product
    queryset = Product.objects.select_related('mat').all()
    template_name = "product_list.html"
    context_object_name = 'products'
    title = "Список товаров"
    
    

class CreateProduct(FormMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'mat']

    template_name = "form.html"
    success_url = reverse_lazy('all-product')
    title = "Форма добавления товара"
    button_text = "Добавить товар"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.label_suffix = ""
        return form

    
class PDFList(DataMixin, ListView):
    model = PDF
    
    context_object_name = 'files'
    template_name = "pdf_list.html"
    title = 'Загруженные файлы'


class CityList(DataMixin, ListView):
    model = City
    
    context_object_name = 'cities'
    template_name = "city_list.html"
    title = "Список городов"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['cities'].exists():
            context['cities'] = populate_cities()
        return context
    
class GraphicsList(DataMixin, ListView):
    model = Graphics
    
    context_object_name = 'charts'
    template_name = "chart_list.html"
    title = "Графики"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['charts'].exists():
            context['charts'] = generate_charts()            
        return context

class DeleteProductView(FormMixin, FormView):
    form_class = DeleteProduct
    template_name = "form.html"
    success_url = reverse_lazy('delete-product')
    
    title = "Форма удаления товара"
    button_text = "Удалить запись"
    
    def form_valid(self, form):
        if not form.is_valid():
            return super().form_invalid(form)
        return super().form_valid(form)
   

class PDFCreateView(FormMixin, FormView):
    form_class = CreatePDF
    template_name = "pawnshop/form_files.html"
    success_url = reverse_lazy('all-pdf')
    
    title = "Форма загрузки файлов"
    button_text = "Загрузить файл на сервер"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    
def download_pdf(request, name):
    obj = get_object_or_404(PDF, name=name)
    response = HttpResponse(obj.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={obj.file.name}'
    return response


class PDFDeleteView(FormMixin, FormView):
    form_class = DeletePDF
    template_name = "form.html"
    success_url = reverse_lazy('all-pdf')
    
    title = "Форма удаления файлов"
    button_text = "Удалить файл"
    
    def form_valid(self, form):
        form.delete()
        return super().form_valid(form)
   
   
class MaterialAPIList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
    
class MaterialAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
    
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class ProductAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
