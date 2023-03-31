import string

from Risco import Risco


class Investimento:
    def __init__(self, name: str, custo: float, retorno: float, risco: Risco):
        self.name = name
        self.custo = custo
        self.retorno = retorno
        self.risco = risco
        self.taxaRetorno = retorno / custo

    def __str__(self):
        return f"{self.name}"
