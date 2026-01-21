from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # właściciel kategorii (relacja do User)
    # CASCADE = jeśli user zostanie usunięty, jego kategorie też znikną
    # related_name= ...  pozwala zrobić: user.categories.all()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self): # co ma się wyświetlać
        return self.name


class Note(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    is_pinned = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # automatycznie ustawiana
    updated_at = models.DateTimeField(auto_now=True) # automatycznie ustawiana

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    # kategoria notatki jest opcjonalna
    # SET_NULL = jeśli kategoria zostanie usunięta, notatka zostaje, a category = NULL
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
