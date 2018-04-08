from django.db import models


MAX_CHAR_FIELD = 256


class Producto(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    stock = models.IntegerField(blank=False, null=True)
    material = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)
    color = models.CharField(max_length=64, blank=False, null=True)
    largo = models.FloatField(blank=False, null=True)
    ancho = models.FloatField(blank=False, null=True)
    alto = models.FloatField(blank=False, null=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.categoria.nombre, self.material, self.color)


class DescripcionProducto(models.Model):
    producto = models.ForeignKey('Producto', related_name='descripciones',
                                 on_delete=models.CASCADE)
    nombre = models.CharField(max_length=MAX_CHAR_FIELD)
    descripcion = models.TextField(blank=False, null=True)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.FloatField(default=0)
    direccion = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)
    departamento = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)
    ciudad = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)
    telefono = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)
    estado = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)


class DetalleCompra(models.Model):
    descripcion_producto = models.ForeignKey('DescripcionProducto', on_delete=models.CASCADE)
    compra = models.ForeignKey('Compra', related_name="detalles", on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False, null=True)
    subtotal = models.FloatField()


class Categoria(models.Model):
    nombre = models.CharField(max_length=MAX_CHAR_FIELD)
    descripcion = models.CharField(max_length=MAX_CHAR_FIELD, blank=False, null=True)

    def __str__(self):
        return self.nombre
