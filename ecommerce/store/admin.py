from django.contrib import admin
from .models import Author, Genre, Book, Cart, CartItem

# Registro del modelo Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registro del modelo Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registro del modelo Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('title', 'author__name', 'genre__name')
    list_filter = ('author', 'genre')
    readonly_fields = ('created_at', 'updated_at')

# Registro del modelo Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'created_at', 'updated_at')
    search_fields = ('user__username', 'session_key')
    readonly_fields = ('created_at', 'updated_at')

# Registro del modelo CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'book', 'quantity', 'created_at', 'updated_at')
    search_fields = ('user__username', 'session_key', 'book__title')
    readonly_fields = ('created_at', 'updated_at')
