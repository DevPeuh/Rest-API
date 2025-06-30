# Validar os dados de entrada e saída da API
from typing import Optional
from ninja import ModelSchema, Schema
from .models import Alunos


class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']

class ProgressoAlunoSchema(Schema):
    nome: str
    email: str
    faixa: str
    aulas_totais: int
    aulas_para_graduacao: int

class AulasConcluidasSchema(Schema):
    quantidade: Optional[int] = 1 
    email_aluno: str
    