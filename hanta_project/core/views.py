from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import RegisterUserForm, ProductForm
from .models import Product
from core.compras import Carrito
from .forms import RegisterUserForm
from .models import Product, Receipt, receiptDetails

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
def products(request):
    if request.user.is_staff != True:
        return redirect('/')
    data = Product.objects.all() 
    return render(request, 'crud/products.html',{"data":data})



def add(request):

    if request.user.is_staff != True:
        return redirect('/')

    if request.method=='POST':
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()         #similar al insert into
            return redirect ('products')
    else:
        productForm = ProductForm()
    return render (request, 'crud/add.html', {'productform': productForm })


def modify(request, id):
    if request.user.is_staff != True:
        return redirect('/')
    
    producto = Product.objects.get(id=id)  
    data ={
        'forModificar': ProductForm(instance=producto), 
        'producto': producto 
    }
    if request.method=='POST':
        formulario = ProductForm(request.POST,request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()           
            return redirect('products')
    return render(request, 'crud/edit.html', data)


def delete(request, id):
    if request.user.is_staff != True:
        return redirect('/')
    
    product = get_object_or_404(Product, id=id)   
    if request.method=='POST':
        if 'delete' in request.POST:
            product.delete()    
            return redirect('products')
    return render(request, 'crud/delete.html', {'product': product})  


def details(request, id):
    if request.user.is_staff != True:
        return redirect('/')
    
    product = get_object_or_404(Product, id=id)   
    return render(request, 'crud/details.html', {'product': product})
    return render(request, 'detalle.html', {'product': product})

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    product = Product.objects.get(id=id)
    carrito_compra.agregar(product=product)
    return redirect('shop')

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    product = Product.objects.get(id=id)
    carrito_compra.eliminar(product=product)
    return redirect('shop')

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    product = Product.objects.get(id=id)
    carrito_compra.restar(product=product)
    return redirect('shop')

def limpiar_producto(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('shop')

def generarBoleta(request):
    total_price=0
    for key, value in request.session['carrito'].items():
        total_price = total_price + int(value['our_price']) * int(value['quantity'])
    receipt = Receipt(total=total_price, status="received")
    receipt.save()
    products = []
    for key, value in request.session['carrito'].items():
            product = Product.objects.get(id = value['id'])
            qty = value['quantity']
            subtotal = qty * int(value['our_price'])
            details = receiptDetails(receipt_id = receipt, product_id = product, quantity = qty, subtotal = subtotal)
            details.save()
            products.append(details)
    datos={
        'products':products,
        'date':receipt.dateBuy,
        'total': receipt.total,
        'status': receipt.status
    }
    request.session['receipt'] = receipt.receipt_id
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'cartdetails.html',datos)

