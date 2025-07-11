
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Bienvenue sur l'API Movie Recommender 🔥"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",  include("movies.urls")),
    path('', root_view), 
    
]
