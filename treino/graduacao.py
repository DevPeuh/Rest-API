import math

ordem_faixa = {'Branca1': 0, 'Cinza': 1, 'Laranja': 2, 'Amarela': 3, 'Verde': 4, 'Azul': 5, 'Roxo': 6, 'Marrom': 7, 'Preta': 8}

def calcular_aulas_para_graduacao(n):
    d = 1.47
    k = 30 / math.log(d)
    aulas = k * math.log(n + d)
    return round(aulas)