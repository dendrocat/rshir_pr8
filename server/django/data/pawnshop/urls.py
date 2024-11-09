from django.urls import path
from .views import *


urlpatterns = [
    path('product/', ProductList.as_view(), name='all-product'),
    path('product/create', CreateProduct.as_view(), name='create-product'),
    path('product/delete', DeleteProductView.as_view(), name='delete-product'),
    path('pdf/', PDFList.as_view(), name='all-pdf'),
    path('pdf/download/<path:name>', download_pdf, name='download-pdf'),
    path('pdf/create/', PDFCreateView.as_view(), name='create-pdf'),
    path('pdf/delete/', PDFDeleteView.as_view(), name='delete-pdf'),
    path('city/', CityList.as_view(), name='all-city'),
    path('graphics/', GraphicsList.as_view(), name='graphics-city'),
 
    path('api/material/', MaterialAPIList.as_view()),
    path('api/material/<int:pk>', MaterialAPIDetail.as_view()),
    path('api/product/', ProductAPIList.as_view()),
    path('api/product/<int:pk>', ProductAPIDetail.as_view())   
]

