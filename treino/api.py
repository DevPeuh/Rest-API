from typing import List
from ninja import Router
from .schemas import AlunosSchema
from .models import Alunos
from ninja.errors import HttpError


treino_router = Router() # agrupar as rotas de treino

@treino_router.post('', response={200: AlunosSchema}) 
def criar_aluno(request, aluno_schema: AlunosSchema):

    if Alunos.objects.filter(email=aluno_schema.email).exists():
        raise HttpError(400, 'Email já cadastrado')
    
    aluno = Alunos(**aluno_schema.dict()) # Descompactar o dicionário e criar o objeto (o aluno)
    aluno.save()
    return aluno

@treino_router.get('/alunos/', response=List[AlunosSchema]) 
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos
