from rest_framework import serializers

from core.models import Producto, Categoria


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    categoria = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre',)
