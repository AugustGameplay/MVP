from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def inicio_sesion(request):
    """
    Vista que maneja tanto el inicio de sesión como el registro de usuarios.
    """
    if request.method == 'POST':
        if 'login' in request.POST:
            # Manejar inicio de sesión
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {user.username}!')
                return redirect('inicio_registro')  # Redirige a la página principal
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        elif 'register' in request.POST:
            # Manejar registro
            full_name = request.POST.get('nombre_completo')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado.')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                )
                user.first_name = full_name  # Guardar el nombre completo
                user.save()
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                return redirect('inicio_registro')  # Redirige para iniciar sesión

    return render(request, 'login.html')

def cerrar_sesion(request):
    """
    Vista para cerrar sesión del usuario.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio_sesion')
def registro(request):
    return render(request, 'registro.html')

# Vista para la página principal (index)
def index(request):
    return render(request, 'index.html')
