from rest_framework import serializers
from .models import Material, Product

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']
        
        
class ProductSerializer(serializers.ModelSerializer):
    mat_id = serializers.PrimaryKeyRelatedField(source='mat', queryset=Material.objects.all())
        
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'mat_id']
    