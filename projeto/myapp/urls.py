from django.urls import path
from myapp import views

urlpatterns = [
    #chama a rota que eu colocar "rota/"
    #name server para dar nome a rota   
    path('', views.home, name='home'),
    path('cadastroUsuario/', views.adicionar_usuario, name='adicionar_usuario'),
    path('listaUsuarios/', views.listar_usuario, name='listar_usuario'),
    path('atualizar/<int:id>/', views.atualizar_usuarios, name='atualizar_usuarios'),
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    path('cadastroEPI/', views.adicionar_epi, name='adicionar_epi'),
    path('listaEpi/', views.listar_epi, name='listar_epi'),
    path('emprestimoEPI/', views.emprestimo_epi, name='emprestimo_epi'),
    path('atualizarEPI/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
    path('deletarepi/<int:id>/', views.deletar_epi, name='deletar_epi'),
]
