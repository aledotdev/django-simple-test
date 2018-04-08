from django.contrib import admin
from django.urls import path
from django.conf import settings

from core.views import CompraFormView, detalle_compra_view

urlpatterns = [
    path('comprar/', CompraFormView.as_view()),
    path('detalle_compra/<int:compra_id>/', detalle_compra_view),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls import include, url
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
