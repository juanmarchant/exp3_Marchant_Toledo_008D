from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect





from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin


from .forms import RegisterUserForm, ProductForm
from .models import Product
from core.compras import Carrito
from .forms import RegisterUserForm, ProfileForm
from .models import Product, Receipt, receiptDetails, Profile

# Create your views here.


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    # subject_template_name = 'registration/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'change/password_reset_confirm.html'
    success_url = reverse_lazy('index')


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/profile_form.html', {'form': form})


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
            user = formy.save()
            Profile.objects.create(user=user)
            user = authenticate(username= formy.cleaned_data['username'] ,
            password = formy.cleaned_data['password1'] )
            login(request, user)
            return redirect('index')
        data['form'] = formy
    return render(request, 'registration/register.html', data)


# @login_required
def shop(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html', {"page_obj": page_obj})

def logout_view(request):
    logout(request)
    return redirect('/')

#CRUD
def products(request):
    if request.user.is_staff != True:
        return redirect('/')
    
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'crud/products.html',{"page_obj":page_obj})

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
    # return render(request, 'detalle.html', {'product': product})

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    product = Product.objects.get(id=id)
    carrito_compra.agregar(product=product)

    previous_url = request.META.get('HTTP_REFERER')
    
    if previous_url:
        return HttpResponseRedirect(previous_url)
    else:
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


def search(request):
    if request.method == "GET":
        search_value = request.GET['q']
        list_games = Product.objects.all().filter(title__contains=search_value)
        
    return render(request, 'search.html', {'list_games': list_games});

@login_required
def generarBoleta(request):
    total_price=0
    for key, value in request.session['carrito'].items():
        total_price = total_price + int(value['our_price']) * int(value['quantity'])
    receipt = Receipt(total=total_price, status="received", user=request.user)
    
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


# Orders
@login_required
def orders(request):
    user = request.user
    all_orders = Receipt.objects.filter(user=user)
    print(request.user, all_orders)
    return render(request, 'orders.html', {'orders': all_orders})



