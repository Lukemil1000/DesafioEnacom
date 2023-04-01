import unittest
from collections import Counter

from Investimento import Investimento
from Otimizador import Otimizador
from Risco import Risco


class TesteOtimizador(unittest.TestCase):
    def teste_otimizador_solucao_minima_maior_que_max_por_risco(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 11, 8, Risco.BAIXO),
                         Investimento("Teste 3", 3, 3.5, Risco.MEDIO),
                         Investimento("Teste 4", 5, 2, Risco.MEDIO),
                         Investimento("Teste 5", 8, 4, Risco.ALTO)]

        max_gasto_risco = {
            Risco.BAIXO: 20,
            Risco.MEDIO: 20,
            Risco.ALTO: 10
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 50

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        self.assertRaises(ValueError, otimizador.solucao_minima)

    def teste_otimizador_solucao_minima_maior_que_orcamento(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 7, 7, Risco.BAIXO),
                         Investimento("Teste 3", 3, 3.5, Risco.MEDIO),
                         Investimento("Teste 4", 5, 2, Risco.MEDIO),
                         Investimento("Teste 5", 10, 4, Risco.ALTO)]

        max_gasto_risco = {
            Risco.BAIXO: 20,
            Risco.MEDIO: 20,
            Risco.ALTO: 10
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 30

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        self.assertRaises(ValueError, otimizador.solucao_minima)

    def teste_otimizador_respeita_minimo_por_risco(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 7, 7, Risco.BAIXO),
                         Investimento("Teste 3", 3, 3.5, Risco.MEDIO),
                         Investimento("Teste 4", 5, 2, Risco.MEDIO),
                         Investimento("Teste 5", 10, 4, Risco.ALTO),
                         Investimento("Teste 6", 1, 1, Risco.ALTO),
                         Investimento("Teste 7", 1, 1, Risco.ALTO),
                         Investimento("Teste 8", 1, 1, Risco.ALTO),
                         Investimento("Teste 9", 1, 1, Risco.BAIXO)]

        max_gasto_risco = {
            Risco.BAIXO: 20,
            Risco.MEDIO: 20,
            Risco.ALTO: 20
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 100

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        possivel = otimizador.solucao_possivel()
        resultado = otimizador.melhor_solucao(possivel)
        otimizado = otimizador.otimizar(resultado)

        minimo = [risco for risco in min_investimento_risco.values()]
        cont_risco = Counter(investimento.risco for investimento in otimizado)
        cont_risco = [valor for valor in cont_risco.values()]

        self.assertGreaterEqual(cont_risco[0], minimo[0])
        self.assertGreaterEqual(cont_risco[1], minimo[1])
        self.assertGreaterEqual(cont_risco[2], minimo[2])

    def teste_otimizador_otimizar_respeita_max_por_risco(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 6, 7, Risco.BAIXO),
                         Investimento("Teste 3", 2, 3.5, Risco.MEDIO),
                         Investimento("Teste 4", 5, 2, Risco.MEDIO),
                         Investimento("Teste 5", 1, 4, Risco.ALTO),
                         Investimento("Teste 6", 10, 50, Risco.ALTO),
                         Investimento("Teste 7", 10, 50, Risco.ALTO),
                         Investimento("Teste 9", 16, 500, Risco.BAIXO),
                         Investimento("Teste 10", 15, 30, Risco.MEDIO)]

        max_gasto_risco = {
            Risco.BAIXO: 17,
            Risco.MEDIO: 30,
            Risco.ALTO: 10
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 100

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        possivel = otimizador.solucao_possivel()
        resultado = otimizador.melhor_solucao(possivel)
        otimizado = otimizador.otimizar(resultado)

        maximo = [risco for risco in max_gasto_risco.values()]
        custo_risco = [sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.BAIXO),
                       sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.MEDIO),
                       sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.ALTO)]

        self.assertLessEqual(custo_risco[0], maximo[0])
        self.assertLessEqual(custo_risco[1], maximo[1])
        self.assertLessEqual(custo_risco[2], maximo[2])

    def teste_otimizador_otimizar_respeita_orcamento(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 6, 7, Risco.BAIXO),
                         Investimento("Teste 3", 2, 3.5, Risco.MEDIO),
                         Investimento("Teste 4", 5, 2, Risco.MEDIO),
                         Investimento("Teste 5", 1, 4, Risco.ALTO),
                         Investimento("Teste 6", 10, 50, Risco.ALTO),
                         Investimento("Teste 7", 10, 50, Risco.ALTO),
                         Investimento("Teste 9", 16, 500, Risco.BAIXO),
                         Investimento("Teste 10", 15, 30, Risco.MEDIO)]

        max_gasto_risco = {
            Risco.BAIXO: 17,
            Risco.MEDIO: 30,
            Risco.ALTO: 10
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 100

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        possivel = otimizador.solucao_possivel()
        resultado = otimizador.melhor_solucao(possivel)
        otimizado = otimizador.otimizar(resultado)

        self.assertLessEqual(sum(investimento.custo for investimento in otimizado), orcamento)

    def teste_otimizador_menos_opçoes_que_min_por_risco(self):
        investimentos = [Investimento("Teste 1", 10, 7, Risco.BAIXO),
                         Investimento("Teste 2", 6, 7, Risco.MEDIO),
                         Investimento("Teste 3", 2, 3.5, Risco.ALTO)]

        max_gasto_risco = {
            Risco.BAIXO: 17,
            Risco.MEDIO: 30,
            Risco.ALTO: 10
        }

        min_investimento_risco = {
            Risco.BAIXO: 2,
            Risco.MEDIO: 2,
            Risco.ALTO: 1
        }

        orcamento = 100

        otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

        self.assertRaises(ValueError, otimizador.solucao_minima)


if __name__ == '__main__':
    unittest.main()
