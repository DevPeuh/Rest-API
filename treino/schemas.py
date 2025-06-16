# Validar os dados de entrada e saída da API
from ninja import ModelSchema, Schema
from .models import Alunos


class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = '__all__'

class ProgressoAlunoSchema(Schema):
    nome: str
    email: str
    faixa: str
    aulas_concluidas: int
    aulas_para_graduacao: int