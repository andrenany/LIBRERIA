from django.core.exceptions import ObjectDoesNotExist

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        
        if not carrito:
            carrito = self.session["carrito"] = {}
        
        self.carrito = carrito

    def agregar(self, book):
        book_id = str(book.id)
        
        try:
            stock_disponible = book.stock
        except ObjectDoesNotExist:
            raise ValueError("El producto no existe en la base de datos.")
        
        if book_id not in self.carrito:
            self.carrito[book_id] = {
                'id': book.id,
                'titulo': book.title,
                'cantidad': 1,
                'acumulado': float(book.price),  # Ensure price is float
            }
        else:
            if stock_disponible <= 0:
                raise ValueError("El producto no tiene stock disponible.")
            self.carrito[book_id]['cantidad'] += 1
            self.carrito[book_id]['acumulado'] += float(book.price)

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, book):
        book_id = str(book.id)
        if book_id in self.carrito:
            del self.carrito[book_id]
            self.guardar_carrito()

    def restar(self, book):
        book_id = str(book.id)
        if book_id in self.carrito:
            if self.carrito[book_id]['cantidad'] > 1:
                self.carrito[book_id]['cantidad'] -= 1
                self.carrito[book_id]['acumulado'] -= float(book.price)
            else:
                del self.carrito[book_id]
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True
