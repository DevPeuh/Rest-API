from ninja import NinjaAPI
from treino.api import treino_router

api = NinjaAPI() # Vai ser o endpoint principal da API
api.add_router('', treino_router)
