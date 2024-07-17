# En views.py dentro de la aplicación store

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Contacto, Author, Genre
from .forms import ContactoForm
from store.Carrito import Carrito

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def autores(request):
    autores = Author.objects.all()
    return render(request, 'autores.html', {'autores': autores})

@login_required
def generos(request):
    generos = Genre.objects.all()
    return render(request, 'generos.html', {'generos': generos})

@login_required
def libros(request):
    libros = Book.objects.all()
    return render(request, 'libros.html', {'libros': libros})

@login_required
def agregar_producto(request, book_id):
    carrito = Carrito(request)
    book = get_object_or_404(Book, id=book_id)
    try:
        carrito.agregar(book)
        # Reducir el stock del libro
        book.stock -= 1
        book.save()
    except ValueError as e:
        # Manejar cualquier excepción específica que desees capturar
        print(f"Error al agregar al carrito: {e}")
    return redirect('view_cart')

@login_required
def eliminar_producto(request, book_id):
    carrito = Carrito(request)
    book = get_object_or_404(Book, id=book_id)
    carrito.eliminar(book)
    # Devolver el stock al eliminar del carrito
    book.stock += 1
    book.save()
    return redirect('view_cart')

@login_required
def restar_producto(request, book_id):
    carrito = Carrito(request)
    book = get_object_or_404(Book, id=book_id)
    carrito.restar(book)
    # Devolver el stock al restar del carrito
    book.stock += 1
    book.save()
    return redirect('view_cart')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('view_cart')

@login_required
def view_cart(request):
    carrito = Carrito(request)
    cart_items = []
    total_acumulado = 0
    for key, value in carrito.carrito.items():
        book = get_object_or_404(Book, id=value['id'])
        total_acumulado += value['acumulado']
        cart_items.append({
            'book': book,
            'cantidad': value['cantidad'],
            'acumulado': value['acumulado']
        })

    return render(request, 'carrito.html', {'cart_items': cart_items, 'total_acumulado': total_acumulado})

@login_required
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

@login_required
def contacto_confirmacion(request):
    return render(request, 'contacto/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

@login_required
def compra_exitosa(request):
    # Lógica para mostrar una página de confirmación de compra exitosa
    return render(request, 'compra_exitosa.html')

@login_required
def realizar_compra(request):
    if request.method == 'POST':
        # Aquí podrías agregar lógica adicional para procesar la compra
        # Por ejemplo, guardar la compra en la base de datos, enviar un correo electrónico de confirmación, etc.
        
        # Limpiar el carrito después de la compra
        carrito = Carrito(request)
        carrito.limpiar_carrito()
        
        # Redirigir a la página de compra exitosa
        return redirect('compra_exitosa')
    else:
        # Si el método no es POST, simplemente redirige al carrito o donde desees
        return redirect('view_cart')

@login_required
def vaciar_carrito(request):
    if 'carrito' in request.session:
        request.session['carrito'] = {}
    return redirect('view_cart')  # O redirige a la página de carrito o donde desees
