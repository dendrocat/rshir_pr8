from django.utils.html import format_html
from urllib.parse import urlencode
from django.contrib import admin
from django.urls import reverse
from .models import *
from .templatetags.size_extra import convert_size


admin.site.site_title = "Админ-панель ломбарда"
admin.site.site_header = "Админ-панель ломбарда"

# Register your models here.
@admin.register(Material)
class MaterialConfig(admin.ModelAdmin): 
    list_display = ("id", "name", "view_product_link")
    list_display_links = ("name", )
    
    def view_product_link(self, obj):
        count = obj.product_set.count()
        url = (
            reverse("admin:pawnshop_product_changelist")
            + "?"
            + urlencode({"mat__id__exact": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} товара(ов)</a>')
    
    view_product_link.short_description = "Количество товаров"


@admin.register(Product)
class ProductConfig(admin.ModelAdmin):
    list_display = ("id", "name", "price", "mat")
    list_display_links = ("name", )
    list_filter = ["mat"]
    
    class Meta:
        ordering = ["pk"]


@admin.register(PDF)
class PDFConfig(admin.ModelAdmin):
    list_display = ['id', 'name', 'show_size']
    list_display_links = ['name']
    readonly_fields = ['size']
    
    def show_size(self, obj):
        return convert_size(obj.size)
    
    show_size.short_description = "Размер файла"
    

@admin.register(City)
class CityConfig(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'number']
    list_display_links = ['name']
    

@admin.register(Graphics)
class GraphicsConfig(admin.ModelAdmin):
    list_display = ['id', 'name', 'show_chart']
    list_display_links = ['name']
    readonly_fields = ['show_chart']
    
    @admin.display(description="График")
    def show_chart(self, graphic: Graphics):
        return format_html(f"<img src={graphic.file.url} width='100%'>")
        