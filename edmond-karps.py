def edmonds_karp(C, inicio, fim):
    n = len(C)  # C e a matriz de capacidade
    F = [[0] * n for _ in range(n)]
    fluxo_min = 0
    # capacidade residual u para v é C[u][v] - F[u][v]

    feito = False

    while not feito:
        caminho = bfs(C, F, inicio, fim)
        if not caminho:
            feito = True
        # ir pelos caminhos para encontrar menor capacidade
        if not feito:
            u, v = caminho[0], caminho[1]
            fluxo = C[u][v] - F[u][v]
            for i in range(len(caminho) - 2):
                u, v = caminho[i+1], caminho[i+2]
                fluxo += C[u][v] - F[u][v]
            # atravessar os caminhos para atualizar o fluxo
            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i+1]
                F[u][v] += fluxo
                F[v][u] -= fluxo
            if(fluxo_min>fluxo or fluxo_min==0):
                fluxo_min=fluxo
    return fluxo_min


def bfs(C, F, inicio, fim):
    P = [-1] * len(C)  # pai na arvore de pesquisa
    P[inicio] = inicio
    fila = [inicio]
    while fila:
        u = fila.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                fila.append(v)
                if v == fim:
                    caminho = []
                    while True:
                        caminho.insert(0, v)
                        if v == inicio:
                            break
                        v = P[v]
                    return caminho
    return None


if __name__ == "__main__":
    matriz = [[0, 1, 0, 0, 10],
              [0, 0, 4, 0, 13],
              [0, 0, 0, 3, 0],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0],

              ]

    print(edmonds_karp(matriz, 0, 4))
