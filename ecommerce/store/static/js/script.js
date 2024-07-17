
function openModal(modalId) {
    var modalElement = document.getElementById(modalId);
    if (modalElement) {
        var modal = new bootstrap.Modal(modalElement);
        modal.show();
    } else {
        console.error('Modal element not found:', modalId);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Log para verificar que el script se está ejecutando
    console.log('DOM fully loaded and parsed');
    
    // Verificar si Bootstrap está disponible
    if (typeof bootstrap !== 'undefined') {
        console.log('Bootstrap is loaded');
    } else {
        console.error('Bootstrap is not loaded');
    }
    
    // Verificar si los elementos de los modales existen
    ['autor1Modal', 'autor2Modal', 'autor3Modal'].forEach(function(modalId) {
        var element = document.getElementById(modalId);
        if (element) {
            console.log('Modal element found:', modalId);
        } else {
            console.error('Modal element not found:', modalId);
        }
    });
});







<script>
    // Datos de los autores (simulados para el ejemplo)
    const autores = [
        {
            id: 1,
            nombre: "Autor 1",
            descripcion: "Descripción detallada del Autor 1."
        },
        {
            id: 2,
            nombre: "Autor 2",
            descripcion: "Descripción detallada del Autor 2."
        },
        {
            id: 3,
            nombre: "Autor 3",
            descripcion: "Descripción detallada del Autor 3."
        }
    ];

    // Función para cargar los detalles del autor en el modal correspondiente
    function cargarDetallesAutor(idAutor, modalId) {
        const autor = autores.find(a => a.id === idAutor);
        if (autor) {
            const modalBody = document.getElementById(modalId);
            modalBody.innerHTML = `
                <img src="{% static 'img/autor${idAutor}.jpg' %}" class="img-fluid" alt="${autor.nombre}">
                <p>${autor.descripcion}</p>
            `;
        }
    }

    // Event listener para cada botón "Ver detalles"
    document.querySelectorAll('.btn-primary').forEach(button => {
        button.addEventListener('click', () => {
            const targetModal = button.getAttribute('data-bs-target');
            const autorId = parseInt(button.getAttribute('data-autor-id'));
            cargarDetallesAutor(autorId, targetModal.substring(1));
            const modal = new bootstrap.Modal(document.querySelector(targetModal));
            modal.show();
        });
    });
</script>
