from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):
    #vaicadrastrar 
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg': 'Cadrastro Realizado com Sucesso'}

    return render(request, 'index.html', contexto)


def sobre(request):
    #vailistarideias
    pessoa = Pessoa.objects.filter(ativo=True).all()
    contexto = {
        'pessoas':pessoa
    }
    return render(request, 'sobre.html', contexto)

def login(request):
    if request.method:'POST' :
        email_form=request.POST.get('email')
        Pessoa = Pessoa.objects.filter(email=email_form).frist ()

        print ('')


