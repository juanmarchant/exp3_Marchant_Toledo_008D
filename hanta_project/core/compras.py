class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, product):
        if product.id not in self.carrito.keys():
            self.carrito[product.id]={
                "id":product.id,
                "title":product.title,
                "our_price":str (product.our_price),
                "quantity": 1,
                "total":product.our_price,
            }
        else:
            for key, value in self.carrito.items():
                if key==product.id:
                    value["quantity"] = value["quantity"]+1
                    value["our_price"] = product.our_price
                    value["total"] = value["total"] + product.our_price
                    break
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, product):
        id = product.id
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, product):
        for key, value in self.carrito.items():
            if key == product.id:
                value["quantity"] = value["quantity"]-1
                value["total"] = int(value["total"])- product.our_price
                if value["quantity"] < 1:
                    self.eliminar(product)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True