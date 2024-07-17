# ecommerce/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from store import views  # Importa tus vistas desde la aplicación store
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluir URLs de autenticación de Django
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('realizar-compra/', views.realizar_compra, name='realizar_compra'),
    path('compra-exitosa/', views.compra_exitosa, name='compra_exitosa'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
