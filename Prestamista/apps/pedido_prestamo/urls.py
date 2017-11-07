from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from apps.pedido_prestamo.views import (index, prestamo_view, prestamo_list,
                                        prestamo_edit, prestamo_delete)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo/$', prestamo_view, name="nuevo_prestamo"),
    url(r'^respuesta/$', prestamo_view, name="respuesta_solicitud"),
    url(r'^listar/$', login_required(prestamo_list), name="listar_prestamos"),
    url(r'^editar/(?P<id_prestamo>\d+)$', login_required(prestamo_edit),
        name="editar_prestamo"),
    url(r'^eliminar/(?P<id_prestamo>\d+)$', login_required(prestamo_delete),
        name="eliminar_prestamo"),
    url(r'^login/$', login,
        {"template_name": "pedido_prestamo/prestamo_login.html"},
        name="login_admin"),
    url(r'^logout$', logout,
        {'next_page': '/prestamos'},
        name="logout_admin")
]
