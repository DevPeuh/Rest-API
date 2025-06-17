from django.db import models


faixas_jiujitsu = [
        ('B', 'Branca'),
        ('C', 'Cinza'),
        ('L', 'Laranja'),
        ('A', 'Amarela'),
        ('V', 'Verde'),
        ('AZ', 'Azul' ),
        ('R', 'Roxo'),
        ('M', 'Marrom'),
        ('P', 'Preta'),
    ]

class Alunos(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    faixa = models.CharField(max_length=2, choices=faixas_jiujitsu, default='B')

    def __str__(self):
        return self.nome
    
class AulasConcluidas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE) # se for deletado, tudo referente a ele também será deletado
    data = models.DateField(auto_now_add=True) 
    faixa_atual = models.CharField(max_length=2, choices=faixas_jiujitsu, default='B')

    def __str__(self):
        return self.aluno.nome + ' - ' + self.data.strftime('%d/%m/%Y') + ' - ' + self.faixa_atual
    
