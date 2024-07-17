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
        if book_id not in self.carrito:
            self.carrito[book_id] = {
                'id': book.id,
                'titulo': book.title,
                'cantidad': 1,
                'acumulado': book.price,
            }
        else:
            self.carrito[book_id]['cantidad'] += 1
            self.carrito[book_id]['acumulado'] += book.price

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
                self.carrito[book_id]['acumulado'] -= book.price
            else:
                del self.carrito[book_id]
            self.guardar_carrito()

    def actualizar_cantidad(self, book, cantidad):
        book_id = str(book.id)
        if book_id in self.carrito:
            self.carrito[book_id]['cantidad'] = cantidad
            self.carrito[book_id]['acumulado'] = cantidad * book.price
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True
