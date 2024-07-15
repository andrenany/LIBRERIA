from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contacto,Author,Genre,Cart,CartItem
from .forms import RegistroForm, ContactoForm

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
##y aca va el detalle
def libro_detalle(request, book_id):
    libro = get_object_or_404(Book, id=book_id)
    return render(request, 'libro_detalle.html', {'libro': libro})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user, session_key=request.session.session_key)
    cart_item, created = CartItem.objects.get_or_create(book=book, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None
        print("No se encontró un carrito para el usuario:", request.user)
    
    context = {
        'cart': cart
    }
    return render(request, 'carrito.html', context)

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

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
