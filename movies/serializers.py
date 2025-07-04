from rest_framework import serializers

from django.contrib.auth.models import User


from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ["id","title", "genres", "rating"]
        
        

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirmez le mot de passe")
    
    
    class Meta:
        model = User
        fields= ["username", "email", "password", "password2"]
        
    
    def validate(self, data):
        if data["password"]!=data["password2"]:
            raise serializers.ValidationError("les mots de passe ne corresponde pas") 
        return data
        
    def create(self, validate_data):
        validate_data.pop("password2")
        user= User.objects.create_user(
            username=validate_data["username"],
            email= validate_data.get("email"),
            password=validate_data["password"]
        )
        return user