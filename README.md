# Notely — Django Notes App
 
Notely is a Django web application for managing notes.
 
---
 
## Features
 
### Notes
- adding notes
- editing / deleting
- pinning notes
- priorities (Low / Normal / High)
- due date
- note detail view
### Categories
- creating categories
- assigning categories to notes
### Tasks (checklist inside a note)
- adding tasks to a note
- marking as done / not done
### REST API (JSON)
- list of user's notes
- single note detail
---
 
## Tech Stack
- Python 3.10+
- Django 5.2.x
- Django REST Framework
- HTML + CSS + JS
---
 
## Installation & Setup (macOS / Linux)
 
### 1) Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
 
### 2) Install dependencies
```bash
pip install -r requirements.txt
```
 
If you run into Django version issues, replace the Django version in `requirements.txt` with an older one, e.g. `4.2.10`.
 
### 3) Run migrations
```bash
python manage.py migrate
```
 
### 4) (Optional) Create an admin account
```bash
python manage.py createsuperuser
```
 
### 5) Start the server
```bash
python manage.py runserver
```
 
The app runs at http://127.0.0.1:8000/
