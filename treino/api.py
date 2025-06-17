from typing import List
from ninja import Router
from .schemas import AlunosSchema, ProgressoAlunoSchema
from .models import Alunos, AulasConcluidas
from ninja.errors import HttpError
from .graduacao import *


treino_router = Router() # agrupar as rotas de treino

@treino_router.post('', response={200: AlunosSchema}) 
def criar_aluno(request, aluno_schema: AlunosSchema):

    if Alunos.objects.filter(email=aluno_schema.email).exists():
        raise HttpError(400, 'Email já cadastrado')
    
    aluno = Alunos(**aluno_schema.dict()) # Descompactar o dicionário e criar o objeto (o aluno)
    aluno.save()
    return aluno

@treino_router.get('/aluno/', response=List[AlunosSchema]) 
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

@treino_router.get('/progresso_aluno/', response={200: ProgressoAlunoSchema})
def progresso_aluno(request, email_aluno: str):
    aluno = Alunos.objects.get(email= email_aluno)
    faixa_atual = aluno.get_faixa_display()
    n = ordem_faixa.get(faixa_atual)
    aulas_para_graduacao = calcular_aulas_para_graduacao(n)
    aulas_concluidas = AulasConcluidas.objects.filter(aluno = aluno, faixa_atual = aluno.faixa).count()
    aulas_faltantes = aulas_para_graduacao - aulas_concluidas

    return {
        'nome': aluno.nome,
        'email': aluno.email,
        'faixa': aluno.faixa,
        'aulas_totais': aulas_concluidas,
        'aulas_para_graduacao': aulas_faltantes
    }