from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Usuario, Epi

# Create your views here.
def home(request):
    return render(request, 'globals/home.html')

def adicionar_usuario(request):
    nome = None;
    if request.method == 'POST':
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        matricula = request.POST.get("matricula")
 # se usuario enviar um nome entao pesquisa no banco atravez da funcao like do sql se tem um usuario no banco com esse nome
 # caso tenha, verifiquei a senha no banco é = a senha mandou na requisição
 #
        if nome and idade and matricula:
            Usuario.objects.create(nome=nome, idade=idade, matricula=matricula)
    return render(request, 'globals/cadastroUsuario.html')

def listar_usuario(request):
    values = Usuario.objects.all()  
    return render(request, 'globals/listaUsuarios.html',{"lista_usuarios":values})

def atualizar_usuarios(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        matricula = request.POST.get("matricula")
        if nome and idade:
            usuario.nome = nome
            usuario.idade = idade
            usuario.matricula = matricula
            usuario.save()
            return redirect(listar_usuario)
    return render(request, 'globals/atualizar.html', {"user":usuario})

def deletar_usuario(request, id):
    usuario_deletado = Usuario.objects.get(id=id)
    usuario_deletado.delete()
    return redirect(listar_usuario)

def adicionar_epi(request):
    nome = None;
    if request.method == 'POST':
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        ca = request.POST.get("ca")
        tipo = request.POST.get("tipo")
        if nome and descricao and ca and tipo:
            Epi.objects.create(nome=nome, descricao=descricao, ca=ca, tipo=tipo)
    return render(request, 'globals/cadastroEPI.html')

def listar_epi(request):
    values = Epi.objects.all()  
    return render(request, 'globals/listaEpi.html',{"lista_epis":values})

def emprestimo_epi(request):
    usuarios = Usuario.objects.all()
    epis_disponiveis = Epi.objects.filter(status='disponível')  # Filtra apenas os EPIs disponíveis
    if request.method == 'POST':
        usuario_id = request.POST.get("usuario_id")
        epi_id = request.POST.get("epi_id")

        if usuario_id and epi_id:
            usuario = get_object_or_404(Usuario, id=usuario_id)
            epi = get_object_or_404(Epi, id=epi_id)

            # Atualiza o status do EPI para "emprestado"
            epi.status = 'emprestado'
            epi.save()

            return redirect(emprestimo_epi)

    return render(request, 'globals/emprestimoEPI.html', {"usuarios": usuarios, "epis_disponiveis": epis_disponiveis})

def atualizar_epi(request, id):
    epi = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        ca = request.POST.get("ca")
        status = request.POST.get("status")
        
        if nome and descricao and ca and status:
            epi.nome = nome
            epi.descricao = descricao
            epi.ca = ca
            epi.status = status
            epi.save()
            return redirect('listar_epi')  # Redirecione para a lista de EPIs ou onde preferir
    return render(request, 'globals/atualizarEPI.html', {"epi": epi})

def deletar_epi(request, id):
    epi_deletado = Epi.objects.get(id=id)
    epi_deletado.delete()
    return redirect(listar_epi)