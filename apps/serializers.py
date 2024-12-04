from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        #fields=('nombre','usuario','contraseña')
        fields = '__all__'