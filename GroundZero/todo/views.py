from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.
def home(request):
    Proveedors = Proveedor.objects.all()
    context = {'Proveedors':Proveedors}
    return render(request, 'todo/home.html', context)


def agregar(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProveedorForm()

    context = {'form':form}
    return render(request, 'todo/agregar.html', context)

def eliminar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedor.delete()
    return redirect("home")

def editar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProveedorForm(instance=proveedor)

    context = {"form" : form}
    return render(request, "todo/editar.html", context)
