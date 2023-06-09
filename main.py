from Investimento import Investimento
from Otimizador import Otimizador
from Risco import Risco


def main():
    investimentos = [Investimento("Ampliação da capacidade do armazém ZDP em 5%", 470_000, 410_000, Risco.BAIXO),
                     Investimento("Ampliação da capacidade do armazém MGL em 7%", 400_000, 330_000, Risco.BAIXO),
                     Investimento("Compra de empilhadeira", 170_000, 140_000, Risco.MEDIO),
                     Investimento("Projeto de P&D I", 270_000, 250_000, Risco.MEDIO),
                     Investimento("Projeto de P&D II", 340_000, 320_000, Risco.MEDIO),
                     Investimento("Aquisição de novos equipamentos", 230_000, 320_000, Risco.MEDIO),
                     Investimento("Capacitação de funcionários", 50_000, 90_000, Risco.MEDIO),
                     Investimento("Ampliação da estrutura de carga rodoviária", 440_000, 190_000, Risco.ALTO),
                     Investimento("Construção de datacenter", 320_000, 120_000, Risco.ALTO),
                     Investimento("Aquisição de empresa concorrente", 800_000, 450_000, Risco.ALTO),
                     Investimento("Compra de serviços em nuvem", 120_000, 80_000, Risco.BAIXO),
                     Investimento("Criação de aplicativo mobile e desktop", 150_000, 120_000, Risco.BAIXO),
                     Investimento("Terceirizar serviço de otimização da logística", 300_000, 380_000, Risco.MEDIO)]

    max_gasto_risco = {
        Risco.BAIXO: 1_200_000,
        Risco.MEDIO: 1_500_000,
        Risco.ALTO: 900_000
    }

    min_investimento_risco = {
        Risco.BAIXO: 2,
        Risco.MEDIO: 2,
        Risco.ALTO: 1
    }

    orcamento = 2_400_000

    otimizador = Otimizador(investimentos, max_gasto_risco, min_investimento_risco, orcamento)

    possivel = otimizador.solucao_possivel()
    resultado = otimizador.melhor_solucao(possivel)
    otimizado = otimizador.otimizar(resultado)

    for investimento in otimizado:
        print(investimento)

    custo = sum(investimento.custo for investimento in otimizado)
    custo_baixo = sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.BAIXO)
    custo_medio = sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.MEDIO)
    custo_alto = sum(investimento.custo for investimento in otimizado if investimento.risco == Risco.ALTO)
    retorno = sum(investimento.retorno for investimento in otimizado)
    retorno_medio = retorno/custo

    print(f"Custo total: {custo}")
    print(f"Custo risco baixo: {custo_baixo}")
    print(f"Custo risco médio: {custo_medio}")
    print(f"Custo risco alto: {custo_alto}")
    print(f"Retorno: {retorno}")
    print(f"Taxa de retorno média: {retorno_medio}")


if __name__ == '__main__':
    main()
