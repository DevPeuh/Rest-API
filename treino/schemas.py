# Validar os dados de entrada e saída da API
from ninja import ModelSchema
from .models import Alunos


class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = '__all__'