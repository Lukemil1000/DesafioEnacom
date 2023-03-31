from itertools import permutations, combinations

from Investimento import Investimento
from Risco import Risco


class Otimizador:

    def __init__(self, investimentos: list[Investimento], max_gasto_risco: dict[Risco, float],
                 min_investimento_risco: dict[Risco, int], orcamento: float):
        self.investimentos = investimentos
        self.max_gasto_risco = max_gasto_risco
        self.min_investimento_risco = min_investimento_risco
        self.orcamento = orcamento

    def solucao_minima(self):
        selecionados = []
        for risco, max in self.max_gasto_risco.items():
            min = self.min_investimento_risco[risco]
            investimentos_desse_risco = [investimento for investimento in self.investimentos if
                                         investimento.risco == risco]
            investimentos_desse_risco.sort(key=lambda x: x.custo)
            investimentos_minimo = investimentos_desse_risco[0:min]
            custo_minimo = sum(investimento.custo for investimento in investimentos_minimo)
            custo_atual = sum(investimento.custo for investimento in selecionados)
            if custo_minimo > max:
                raise ValueError(f"Não existe solução. O custo mínimo do risco {risco} é maior que o teto")
            if custo_minimo + custo_atual > self.orcamento:
                raise ValueError(
                    "Não existe solução. É impossível escolher o número mínimo de investimentos sem exceder o orçamento")

    def solucao_inicial(self) -> list[Investimento]:

        self.solucao_minima()
        selecionados = []
        for risco, max in self.max_gasto_risco.items():
            min = self.min_investimento_risco[risco]
            investimentos_desse_risco = [investimento for investimento in self.investimentos if
                                         investimento.risco == risco]
            investimentos_desse_risco.sort(key=lambda x: x.custo)
            combinacoes = combinations(investimentos_desse_risco, min)
            ideal = 0
            custo_atual = sum(investimento.custo for investimento in selecionados)
            for combinacao in combinacoes:
                custo = sum(investimento.custo for investimento in combinacao)
                if custo < max and custo_atual + custo < self.orcamento:
                    taxa = sum(investimento.taxaRetorno for investimento in combinacao)
                    if taxa > ideal:
                        selecionados_risco = combinacao
                        ideal = taxa
            for selecionado in selecionados_risco:
                selecionados.append(selecionado)
        return selecionados
