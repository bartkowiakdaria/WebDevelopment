document.addEventListener('DOMContentLoaded', () => {
    const filterInput = document.getElementById('note-filter');
    const noteList = document.getElementById('note-list');
    const refreshButton = document.getElementById('refresh-notes');

    if (noteList) {
        var items = Array.from(noteList.getElementsByClassName('note-item')); // var, bo później nadpisujemy items po odświeżeniu listy
    }

    // FILTROWANIE PO TYTULE
    if (filterInput && noteList) {
        // Reagujemy na pisanie w polu input:
        filterInput.addEventListener('input', () => {
            const query = filterInput.value.toLowerCase().trim();
            // przechodzimy po wszystkich notatkach i chowamy te, które nie pasują
            items.forEach(item => {
                const titleElement = item.querySelector('h2'); // tytuly notatek sa w <h2>
                const titleText = titleElement ? titleElement.textContent.toLowerCase() : '';

                // jeśli query puste -> pokazujemy wszystkie
                // jeśli query istnieje -> pokazujemy tylko te, które zawierają query w title
                item.style.display = (!query || titleText.includes(query)) ? '' : 'none';
            });
        });
    }

    // AJAX

    const priorityLabels = {
    1: "Low",
    2: "Normal",
    3: "High",
};

    if (refreshButton && noteList) {
        refreshButton.addEventListener('click', () => {
            fetch('/api/notes/')// pobieramy notatki z endpointu API (json)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Błąd sieci: ' + response.status);
                    }
                    return response.json();
                })
                .then(data => {
                    noteList.innerHTML = ''; // zzyścimy aktualną listę notatek w html

                    // dla każdej notatki z api budujemy elementy html
                    data.forEach(note => {
                        const item = document.createElement('div');
                        item.className = 'note-item';

                        const link = document.createElement('a');
                        link.href = `/notes/${note.id}/`;

                        const card = document.createElement('div');
                        card.className = 'note-card';

                        const header = document.createElement('div');
                        header.className = 'note-card-header';

                        const title = document.createElement('h2');
                        title.className = 'note-title';
                        title.textContent = note.title;

                        const priority = document.createElement('span');
                        priority.className = `note-priority note-priority-${note.priority}`;
                        priority.textContent = priorityLabels[note.priority] || note.priority;


                        header.appendChild(title);
                        header.appendChild(priority);
                        card.appendChild(header);
                        link.appendChild(card);
                        item.appendChild(link);
                        noteList.appendChild(item);
                    });

                    // aktualizujemy items, bo lista notatek została przebudowana od zera
                    items = Array.from(noteList.getElementsByClassName('note-item'));
                })
                .catch(error => {
                    console.error('Błąd pobierania notatek:', error);
                    alert('Nie udało się pobrać notatek z API.');
                });
        });
    }
});
