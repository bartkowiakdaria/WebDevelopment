from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note, Category, Task


class RegisterForm(UserCreationForm):
    # dokładamy pole email bo UserCreationForm domyślnie go nie wymaga
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # pola widoczne w formularzu rejestracji
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Nazwa użytkownika"
        self.fields["email"].label = "E-mail"
        self.fields["password1"].label = "Hasło"
        self.fields["password2"].label = "Powtórz hasło"

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'priority', 'is_pinned', 'due_date', 'category'] # pola, które użytkownik może edytować w notatce

    def __init__(self, *args, **kwargs):
        # pobieramy usera przekazanego z widoku
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs) #inicjalizacja formularza

        # żeby w polach category były tylko obiekty tego użytkownika
        if user is not None:
            self.fields['category'].queryset = self.fields['category'].queryset.filter(owner=user)

    # walidacja pola title: obcinamy spacje i sprawdzamy czy nie jest puste
    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError('Tytuł nie może być pusty.')
        return title

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'is_done']