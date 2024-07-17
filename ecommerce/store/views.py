from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contacto,Author,Genre, Cart,CartItem
from .forms import ContactoForm
from store.Carrito import Carrito

##este muestra el index.html
def index(request):
    return render(request, 'index.html')

##este muestra los autores
def autores(request):
    autores = Author.objects.all()
    return render(request, 'autores.html', {'autores': autores})
##y este muestra los generos, no tan necesario, se podria borrar
def generos(request):
    generos = Genre.objects.all()
    return render(request, 'generos.html', {'generos': generos})
##este muestra los libro
def libros(request):
    libros = Book.objects.all()
    return render(request, 'libros.html', {'libros': libros})


def agregar_producto(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def eliminar_producto(request, book_id):
    cart_item = get_object_or_404(CartItem, id=book_id)  # Asegura que book_id corresponde al ID de CartItem
    cart_item.delete()  # Elimina el CartItem encontrado
    return redirect('view_cart')  # Redirige de vuelta a la vista del carrito

def restar_producto(request, book_id):
    carrito = Carrito(request)
    book = get_object_or_404(Book, id=book_id)
    carrito.restar_cantidad(book)
    return redirect('view_cart')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('view_cart')

def view_cart(request):
    return render(request, 'carrito.html')

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'contacto/contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contacto/contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contacto/contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'contacto/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')
