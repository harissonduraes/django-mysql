from django.shortcuts import render
from .forms import ProdutoModelForm
from.models import Produto
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request,'index.html',context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #prod = form.save(commit=False)
                #print(f'Nome:{prod.nome}')
                #print(f'Preço:{prod.preco}')
                #print(f'Estoque:{prod.estoque}')
                #print(f'Imagem:{prod.imagem}')
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else: messages.error(request, 'Erro ao salvar produto')
        else: form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request,'produto.html', context)
    else:
        return redirect('index')