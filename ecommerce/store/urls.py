from django.urls import path, include
from store import views
from django.contrib.auth import views as auth_views
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito


urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.autores, name='autores'),
    path('generos/', views.generos, name='generos'),
    path('libros/', views.libros, name='libros'),
    path('agregar/<int:book_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar/<int:book_id>/', eliminar_producto, name='eliminar_producto'),
    path('restar/<int:book_id>/', restar_producto, name='restar_producto'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
    path('carrito/', views.view_cart, name='view_cart'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Rutas para Contacto
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),

    # Nueva URL protegida
    path('vista_protegida/', views.vista_protegida, name='vista_protegida'),

    # Comentada pero añadida para referencia futura
    # path('registro/', views.registro, name='registro'),
]
