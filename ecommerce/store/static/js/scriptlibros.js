$(document).ready(function() {
    // Captura del evento de clic en el botón "Añadir al Carrito"
    $('.btn-add-to-cart').click(function() {
        var book_id = $(this).data('book-id');
        var url = $(this).data('url'); // Obtiene la URL dinámica desde el atributo data-url

        // Envío de solicitud AJAX para agregar el producto al carrito
        $.ajax({
            type: 'GET',  // Puedes cambiar a 'POST' si es necesario
            url: url.replace('0', book_id), // Usa la URL dinámica obtenida desde data-url
            success: function(response) {
                // Manejo de éxito: podrías mostrar un mensaje, actualizar contador, etc.
                console.log('Producto agregado al carrito');
                alert('Producto agregado al carrito');
            },
            error: function(error) {
                console.log('Error al agregar producto al carrito');
                alert('Error al agregar producto al carrito');
            }
        });
    });
});

    var myModal = new bootstrap.Modal(document.getElementById('bookDetailModal'), {
        keyboard: false
    });

    document.querySelectorAll('.btn-show-details').forEach(item => {
        item.addEventListener('click', event => {
            var bookId = item.getAttribute('data-book-id');
            var bookTitle = item.getAttribute('data-book-title');
            var bookDescription = item.getAttribute('data-book-description');
            var bookAuthor = item.getAttribute('data-book-author');
            var bookGenre = item.getAttribute('data-book-genre');

            document.getElementById('bookTitle').innerText = bookTitle;
            document.getElementById('bookDescription').innerText = bookDescription;
            document.getElementById('bookAuthor').innerText = 'Autor: ' + bookAuthor;
            document.getElementById('bookGenre').innerText = 'Género: ' + bookGenre;

            myModal.show();
        });
    });

