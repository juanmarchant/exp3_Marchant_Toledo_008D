def total_carrito(request):
    total = 0
    if request.user in request.session:
        try:
            for key, value in request.session['carrito'].items():
                total = total + (int(value['our_price']))*(value['quantity'])
        except KeyError:
            request.session['carrito']={}
            total = 0
    return {'total_carrito':int(total)}