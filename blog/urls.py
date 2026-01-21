from django.urls import path
from . import views, api_views


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.note_create, name='note_create'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/<int:pk>/edit/', views.note_update, name='note_update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('register/', views.register, name='register'),
    path('api/notes/', api_views.notes_list_api, name='notes_list_api'),
    path('api/notes/<int:pk>/', api_views.note_detail_api, name='note_detail_api'),
    path('categories/add/', views.category_create, name='category_create'),
    path('notes/<int:note_pk>/tasks/add/', views.task_add, name='task_add'),
    path('tasks/<int:pk>/toggle/', views.task_toggle_done, name='task_toggle_done'),
]
