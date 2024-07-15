from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField  # ETAPA 5
from .utils import encrypt_message, decrypt_message

# MODELO AUTOR
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name

# MODELO GÉNERO
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# MODELO LIBRO
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='books/')
    stock = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# MODELO CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()  # Campo para el mensaje original
    mensaje_cifrado = models.TextField()  # Campo para almacenar el mensaje cifrado
    fecha = models.DateTimeField(auto_now_add=True)  # Añade el campo de fecha

    def save(self, *args, **kwargs):
        # Cifra el mensaje antes de guardarlo
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

    def get_mensaje(self):
        # Descifra el mensaje al recuperarlo
        return decrypt_message(self.mensaje_cifrado)

    def __str__(self):
        return self.nombre

# MODELO CARRITO
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    items = models.ManyToManyField('CartItem', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart ({self.id})"

# MODELO ITEM DEL CARRITO
class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} (x{self.quantity})"
