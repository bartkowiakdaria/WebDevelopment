
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # gotowe widoki logowania/wylogowania/resetu hasła od Django
    path('', include('blog.urls', namespace='blog')), # podpina url-e aplikacji pod główny adres strony
]
