from django.db import models

class Alunos(models.Model):
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
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    faixa = models.CharField(max_length=2, choices=faixas_jiujitsu, default='B')

    def __str__(self):
        return self.nome