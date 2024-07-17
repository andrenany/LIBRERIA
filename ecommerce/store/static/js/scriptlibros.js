document.addEventListener('DOMContentLoaded', function () {
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Escuchar clics en los botones "Agregar al Carrito"
    var addToCartButtons = document.querySelectorAll('.btn-add-to-cart');
    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var bookId = button.getAttribute('data-book-id');

            // Realizar la solicitud POST al servidor
            fetch(`/add_to_cart/${bookId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ book_id: bookId }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('La respuesta del servidor no fue correcta');
                }
                return response.json();
            })
            .then(data => {
                console.log('Respuesta del servidor:', data);
                alert('Libro agregado al carrito correctamente');
                // Puedes actualizar dinámicamente la interfaz de usuario del carrito aquí si es necesario

            })
            .catch(error => {
                console.error('Error al agregar al carrito:', error);
                alert('Error al agregar al carrito');
            });
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var bookDetailModal = new bootstrap.Modal(document.getElementById('bookDetailModal'));

    // Escuchar clics en los botones "Ver Detalle"
    var showDetailButtons = document.querySelectorAll('.btn-show-details');
    showDetailButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var bookTitle = button.getAttribute('data-book-title');
            var bookDescription = button.getAttribute('data-book-description');
            var bookAuthor = button.getAttribute('data-book-author');
            var bookGenre = button.getAttribute('data-book-genre');

            // Actualizar contenido del modal
            document.getElementById('bookTitle').textContent = bookTitle;
            document.getElementById('bookDescription').textContent = bookDescription;
            document.getElementById('bookAuthor').textContent = 'Autor: ' + bookAuthor;
            document.getElementById('bookGenre').textContent = 'Género: ' + bookGenre;

            // Abrir el modal
            bookDetailModal.show();
        });
    });
});
