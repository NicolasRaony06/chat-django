from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import add_message, constants
from .models import Usuario
from django.contrib import auth
from django.contrib.auth.models import User

def cadastrar(request):
    if request.method == 'GET':
        return render(request, "cadastro.html")

    if request.method == 'POST':
        username = str(request.POST.get("username")).title().lstrip()
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            add_message(request, constants.ERROR, "A senhas não são iguais!")
            return redirect("/usuario/cadastrar")

        if not len(senha) >= 6:
            add_message(request, constants.INFO, "A senha deve ter no mínimo 6 caracteres")
            return redirect("/usuario/cadastrar")

        user_username = User.objects.filter(username=username)

        if user_username.exists():
            add_message(request, constants.ERROR, "Este usuário já existe!")
            return redirect("/usuario/cadastrar")

        user = User.objects.create_user(
            username=username,
            password=senha,
        )

        add_message(request, constants.SUCCESS, "Cadastro feito com sucesso!")
        return redirect("/")

    #return HttpResponse('Olá Mundo!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            add_message(request, constants.SUCCESS, "Login feito com sucesso!")
            return redirect("/")
        
        add_message(request, constants.ERROR, "Usuário ou senha estão errados!")
        return redirect("/usuario/login")

    # return HttpResponse("olá mundo")
