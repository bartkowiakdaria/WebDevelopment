# Notely — Django Notes App

Notely to aplikacja webowa napisana w Django do zarządzania notatkami.

---
## Funkcjonalności

### Notatki
- dodawanie notatek
- edycja/usuwanie
- przypinanie notatek 
- priorytety (Low / Normal / High)
- termin wykonania
- widok szczegółów notatki

### Kategorie
- tworzenie kategorii
- przypisywanie kategorii do notatek

### Taski (zadania w notatce)
- dodawanie zadania do notatki
- oznaczanie jako wykonane / niewykonane

### REST API (JSON)
- lista notatek użytkownika
- szczegóły pojedynczej notatki

---

## Technologie
- Python 3.10+
- Django 5.2.x
- Django REST Framework
- HTML + CSS + JS

---

# Instalacja i uruchomienie (macOS / Linux)

## 1) Utwórz środowisko wirtualne (venv)

```bash
python3 -m venv .venv
source .venv/bin/activate
```
## 2) Zainstaluj zależności
```bash
pip install -r requirements.txt
```

## 3) Migracja danych
```bash
python manage.py migrate
```

## 4) (Opcjonalnie) utwórz konto administratora
```bash
python manage.py createsuperuser
```

## 5) Uruchom serwer
```bash
python manage.py runserver
```