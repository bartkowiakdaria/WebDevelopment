from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Category, Task
from django.http import Http404
from django.contrib.auth import login
from .forms import NoteForm, RegisterForm, CategoryForm, TaskForm


def home(request):
    return render(request, 'blog/home.html')

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user).order_by('-is_pinned', '-updated_at')
    return render(request, 'blog/note_list.html', {'notes': notes}) # renderujemu listę notatek

@login_required
def note_create(request):
    if request.method == 'POST': # jeśli formularz został wysłany
        form = NoteForm(request.POST, user=request.user) # przekazujemy usera do NoteForm, żeby filtrował kategorie usera
        if form.is_valid():
            note = form.save(commit=False) # tworzy obiekt Note, ale jeszcze nie zapisuje do bazy
            note.owner = request.user
            note.save()
            form.save_m2m()
            return redirect('blog:note_list') # po zapisie wracamy do listy notatek
    else:
        form = NoteForm(user=request.user) # GET: pokazujemy pusty formularz

    return render(request, 'blog/note_form.html', {'form': form}) # renderujemy template formularza


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user) # pobieramy notatkę tylko jeśli należy do usera (inaczej 404)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=request.user) # instance=note -> edytujemy istniejącą notatkę
        if form.is_valid():
            form.save()
            return redirect('blog:note_list')
    else:
        form = NoteForm(instance=note, user=request.user) # GET: wypełniony formularz danymi notatki

    return render(request, 'blog/note_form.html', {'form': form, 'note': note})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    return render(request, 'blog/note_detail.html', {'note': note})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('blog:note_list')

    # GET: ekran potwierdzenia usunięcia
    return render(request, 'blog/note_confirm_delete.html', {'note': note})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) # formularz z danymi rejestracji
        if form.is_valid():
            user = form.save() # tworzymy użytkownika w bazie
            login(request, user)
            return redirect('blog:note_list')
    else:
        form = RegisterForm() # GET: pusty formularz rejestracji
    return render(request, 'registration/register.html', {'form': form})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            return redirect('blog:note_create')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {'form': form})

@login_required
def task_add(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, owner=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.note = note
            task.owner = request.user
            task.save()
            return redirect('blog:note_detail', pk=note.pk)
    else:
        form = TaskForm()

    return render(request, 'blog/task_form.html', {'form': form, 'note': note})

@login_required
def task_toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.is_done = not task.is_done # zmiana na przeciwną wartość (True -> False i False -> True)
    task.save()
    return redirect('blog:note_detail', pk=task.note.pk)
