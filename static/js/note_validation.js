document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('note-form');
    if (!form) return;

    const titleInput = document.getElementById('id_title'); // Django domyślnie nadaje id_... dla pól
    const contentInput = document.getElementById('id_content');
    const priorityInput = document.getElementById('id_priority');


    // usuwamy wcześniejsze błędy dodane przez JS (żeby nie duplikować komunikatów)
    function clearErrors() {
        form.querySelectorAll('.js-error').forEach(el => el.remove());
    }

    // tworzymy i wyświetlamy komunikat błędu pod danym polem
    function showError(input, message) {
        const error = document.createElement('div');
        error.className = 'js-error error';
        error.textContent = message;
        input.parentNode.appendChild(error);
    }

    form.addEventListener('submit', (event) => {
        clearErrors();
        let valid = true;

        if (titleInput && titleInput.value.trim() === '') {
            showError(titleInput, 'Tytuł jest wymagany.');
            valid = false;
        }

        if (contentInput && contentInput.value.trim().length < 10) {
            showError(contentInput, 'Treść musi mieć co najmniej 10 znaków.');
            valid = false;
        }

        if (!valid) { // jeśli formularz jest niepoprawny -> nie zrobi się POST
            event.preventDefault();
        }
    });
});
