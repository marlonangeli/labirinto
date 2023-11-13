from algoritmos.a_estrela import AEstrela
from algoritmos.busca_gulosa import BuscaGulosa
from modelos.grafo import Grafo
from utils.gerar_mapa import gerar_mapa


def main():
    print('=' * 30)
    print('Benchmark')
    print('=' * 30, '\n\n')

    def relacao_recompensas(coletadas: int, totais: int) -> str:
        if totais/2 <= coletadas:
            return 'Nerdola'
        elif totais/4 <= coletadas:
            return 'Meia boca'
        else:
            return 'Noob'

    parametros = [
        ('Pequeno', 11),
        ('Médio', 17),
        ('Grande', 21)
    ]

    for tamanho, dimensao in parametros:
        for metodo in ['A*', 'Gulosa-']:
            print(f'\nMétodo: {metodo} - Tamanho: {tamanho}')
            mapa = gerar_mapa(dimensao, dimensao, prob_recompensa=0.05)
            grafo = Grafo(mapa)
            if metodo == 'A*':
                a_estrela = AEstrela(grafo)
                caminho = a_estrela.encontrar_caminho()
                dados = a_estrela.dados_ultima_execucao
            elif metodo == 'Gulosa':
                gulosa = BuscaGulosa(grafo)
                caminho = gulosa.encontrar_caminho()
                dados = gulosa.dados_ultima_execucao
            else:
                print('Método não encontrado')
                continue
            if caminho is None:
                print('Não foi possível encontrar um caminho')
            else:
                print(f'Custo total: {dados["custo_total"]} Pesos Argentinos  *cálculo de custo não considera recompensas (e tá um pouco bugado)')
                print(f'Recompensas coletadas: {dados["recompensas_coletadas"]}/{dados["recompensas_totais"]} - {relacao_recompensas(dados["recompensas_coletadas"], dados["recompensas_totais"])}')
                print(f'Nós expandidos: {dados["nos_expandidos"]}')
                print(f'Nós visitados: {dados["nos_visitados"]}')
                print(f'Tempo de execução: {dados["tempo_execucao"]:0.2f} UTR (Unidade de Tempo Rápido)')
                print(f'Memória: {dados["memoria"]} QI (Quilobytes de Informação)')

                print('-' * 30)


if __name__ == '__main__':
    main()
