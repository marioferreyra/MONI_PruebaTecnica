from django.shortcuts import render, redirect
# from django.http import HttpResponse

from apps.pedido_prestamo.forms import PrestamoForm

import apps.pedido_prestamo.services as services

from apps.pedido_prestamo.models import Prestamo
# Create your views here.


def index(request):
    # return HttpResponse("Hola mundo!")
    return render(request, "index.html", {})


def prestamo_view(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)

        if form.is_valid():
            solicitud = form.save()

            is_error, is_approved = services.borrow_money(solicitud.dni,
                                                          solicitud.genero,
                                                          solicitud.email)

            contexto = {
                "user_dni": solicitud.dni,
                "user_nombre": solicitud.nombre,
                "user_apellido": solicitud.apellido,
                "user_genero": solicitud.genero,
                "user_email": solicitud.email,
                "user_monto": solicitud.monto,
                "is_solicitud_error": is_error,
                "is_solicitud_approved": is_approved
            }

            return render(request, "pedido_prestamo/prestamo_respuesta.html",
                          {"contexto": contexto})

        return redirect("prestamos:nuevo_prestamo")
    else:
        form = PrestamoForm()

    return render(request, "pedido_prestamo/prestamo_form.html",
                  {"form": form})


def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    contexto = {"prestamos": prestamos}

    return render(request, "pedido_prestamo/prestamo_list.html", contexto)


def prestamo_edit(request, id_prestamo):
    prestamo = Prestamo.objects.get(id=id_prestamo)
    if request.method == "GET":
        form = PrestamoForm(instance=prestamo)
    else:
        form = PrestamoForm(request.POST, instance=prestamo)

        if form.is_valid():
            form.save()

        return redirect("prestamos:listar_prestamos")

    return render(request, "pedido_prestamo/prestamo_form.html",
                  {"form": form})


def prestamo_delete(request, id_prestamo):
    prestamo = Prestamo.objects.get(id=id_prestamo)
    if request.method == "POST":
        prestamo.delete()

        return redirect("prestamos:listar_prestamos")

    return render(request, "pedido_prestamo/prestamo_delete.html",
                  {"prestamo": prestamo})
