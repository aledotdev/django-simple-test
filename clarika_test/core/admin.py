from django.contrib import admin


from . import models as core_models


class DescripcionProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'producto', 'precio')


class ProductoAdmin(admin.ModelAdmin):

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductoAdmin, self).get_queryset(*args, **kwargs)
        return qs.select_related('categoria')


class DetalleCompraInlineAdmin(admin.TabularInline):
    model = core_models.DetalleCompra
    readonly_fields = ('precio_unitario',)

    def precio_unitario(self, obj):
        return "$%s" % obj.descripcion_producto.precio


class ComprasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'total')
    inlines = [DetalleCompraInlineAdmin]


admin.site.register(core_models.Categoria)
admin.site.register(core_models.Producto, ProductoAdmin)
admin.site.register(core_models.DescripcionProducto, DescripcionProductoAdmin)
admin.site.register(core_models.Compra, ComprasAdmin)
admin.site.register(core_models.DetalleCompra)
