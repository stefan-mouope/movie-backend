from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response 

from .models import Movie

from .serializers import MovieSerializer, RegisterSerializer

from .recommendations import get_recommendations

from django.contrib.auth.models import User


class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer


class ProtectedView(APIView):
    permission_classes=IsAuthenticated
    
    def get(self, request):
        return Response({"message": f"Bonjour {request.user.username}, vous êtes connecté !"})





class MoviesListView(APIView):
    
    def get(self ,request):
        movies= Movie.objects.all()
        serializer= MovieSerializer(movies, many= True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    

class RecommendationsView(APIView):
    def get( self, request, movie_id):
        try:
            Movie.objects.get(id=movie_id) 
            recocommendations= get_recommendations(movie_id)
            return Response(recocommendations)
        except Movie.DoesNotExist:
            return Response ({"erreur : ": " Film non Trouve"}, status= 404)
        
        