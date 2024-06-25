from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from .forms import RegisterUserForm
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    data = {
        'form': RegisterUserForm()
    }
    if request.method == 'POST':
        formy = RegisterUserForm(data=request.POST)
        if formy.is_valid():
            formy.save()
            user = authenticate(username= formy.cleaned_data['username'] ,
            password = formy.cleaned_data['password1'] )
            login(request, user)
            return redirect('index')
        data['form'] = formy
    return render(request, 'registration/register.html', data)


# @login_required
def shop(request):
    data = Product.objects.all() 
    return render(request, 'shop.html', {"data":data})

def logout_view(request):
    logout(request)
    return redirect('/')


#CRUD
@login_required
def products(request):
    data = Product.objects.all() 
    return render(request, 'crud/products.html',{"data":data})


def modify(request, id):
    # producto = Product.objects.get(id=id)  #busca un obj por medio del id
    # data ={
    #     'forModificar': VehiculoForm(instance=producto), #devuelve un objeto tipo form con el vehiculo encontrado
    #     'vehiculo': producto 
    # }
    # if request.method=='POST':
    #     formulario = VehiculoForm(request.POST,request.FILES,instance=vehiculo)
    #     if formulario.is_valid():
    #         formulario.save()           #permite actualizar un objeto
    #         return redirect('productos')
    return render(request, 'crud/edit.html')

def delete(request, id):
    product = get_object_or_404(Product, idVehiculo=id)   #buscamos un obj por medio del id
    if request.method=='POST':
        if 'delete' in request.POST:
            product.delete()           #eliminamos un objeto
            return redirect('products')
    return render(request, 'crud/delete.html', {'product': product})  


def details(request, id):
    product = get_object_or_404(Product, id=id)   
    return render(request, 'detalle.html', {'product': product})