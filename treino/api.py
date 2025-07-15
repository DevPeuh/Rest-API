from typing import List
from ninja import Router
from .schemas import AlunosSchema, ProgressoAlunoSchema, AulasConcluidasSchema
from .models import Alunos, AulasConcluidas
from ninja.errors import HttpError
from .graduacao import *
from datetime import date


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


@treino_router.post('/aulas_concluidas/', response={200: AulasConcluidasSchema}) 
def aulas_concluidas(request, aula_realizada: AulasConcluidasSchema):
    quantidade = aulas_concluidas.dict()['quantidade']
    email_aluno = aulas_concluidas.dict()['email_aluno']

    if quantidade < 1:
        raise HttpError(400, 'Quantidade de aulas concluídas inválida.')
    
    for ac in range(quantidade):
        aluno = Alunos.objects.get(email=email_aluno)
        aulas_concluidas = AulasConcluidas(aluno=aluno, faixa_atual=aluno.faixa)
        aulas_concluidas.save()

    return 200, f'Aula concluída com sucesso. Total de aulas concluídas: {quantidade} - {aluno.nome}'

@treino_router.put('/alunos/{aluno_id}/', response={200: AlunosSchema})
def atualizar_aluno(request, aluno_id: int, aluno_schema: AlunosSchema):
    aluno = Alunos.objects.get(id=aluno_id)
    if not aluno:
        raise HttpError(404, 'ALuno não encontrado')
    idade = date.today() - aluno.data_nascimento
    if int(idade.days/365) < 18 and aluno_schema.dict()['faixa'] in ['AZ', 'R', 'M', 'P']: 
        raise HttpError(400, 'Alunor menor de idade não pode ter faixa azul, roxa, marrom ou preta.')
    
    for key, value in aluno_schema.dict().items(): 
        if value:
            setattr(aluno, key, value) # Atualiza o atributo do aluno com o valor do schema
        
        aluno.save()
        return aluno
    
    