from django.db import models

# Create your models here.
# aqui é criado o que é salvo no banco de dados;

class  Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    matricula = models.IntegerField()

    def __str__(self):
        return f"Usuario: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}"
    
class Epi(models.Model):
    STATUS_CHOICES = [
        ('disponível', 'Disponível'),
        ('emprestado', 'Emprestado'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponível')