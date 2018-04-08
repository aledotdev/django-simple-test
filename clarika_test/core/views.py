from django.shortcuts import render
from django.views import View
from django.utils import timezone

from .models import Producto, Compra, DetalleCompra, DescripcionProducto


def detalle_compra_view(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    return render(request, 'detalle_compra.html', dict(compra=compra, user=request.user))


class CompraFormView(View):

    def get(self, request):
        productos = Producto.objects\
            .select_related('categoria').prefetch_related('descripciones')\
            .order_by('categoria__nombre').all()
        return render(request, 'compra.html', dict(productos=productos))

    def post(self, request):
        compra = Compra.objects.create(usuario=request.user, fecha=timezone.now())

        precio_total = 0.0
        for desc_producto_id, cantidad in parse_productos(request.POST):
            desc_producto = DescripcionProducto.objects.get(id=desc_producto_id)
            subtotal = desc_producto.precio * cantidad
            DetalleCompra.objects.create(
                compra=compra,
                descripcion_producto=desc_producto,
                cantidad=cantidad,
                subtotal=subtotal)
            precio_total = precio_total + subtotal

        compra.total = precio_total
        compra.save()

        return self.get(request)


def parse_productos(data):
    productos = []
    for key, value in data.items():
        if not key.startswith('producto-'):
            continue

        desc_producto_id = int(key.replace('producto-', ''))
        value = int(value)

        if value > 0:
            productos.append((desc_producto_id, value))

    return productos
