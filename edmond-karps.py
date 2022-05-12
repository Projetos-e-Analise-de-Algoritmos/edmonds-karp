import decimal


def EdmondsKarp(E, C, s, t):
    n = len(C)
    flow = 0
    F = [[0 for y in range(n)] for x in range(n)]
    while True:
        P = [-1 for x in range(n)]
        P[s] = -2
        M = [0 for x in range(n)]
        M[s] = decimal.Decimal('Infinity')
        BFSq = []
        BFSq.append(s)
        pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
        if pathFlow == 0:
            break
        flow = flow + pathFlow
        v = t
        while v != s:
            u = P[v]
            F[u][v] = F[u][v] + pathFlow
            F[v][u] = F[v][u] - pathFlow
            v = u
    return flow


def BFSEK(E, C, s, t, F, P, M, BFSq):
    while (len(BFSq) > 0):
        u = BFSq.pop(0)
        for v in E[u]:
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t:
                    BFSq.append(v)
                else:
                    return M[t], P
    return 0, P


if __name__ == "__main__":
    matriz = [[0, 1, 0, 1, 0],
              [0, 0, 1, 0, 0],
              [1, 0, 0, 1, 1],
              [0, 1, 0, 0, 1],
              [0, 0, 0, 0, 0],
              ]

    matriz1 = [[0, 3, 0, 3, 0],
               [0, 0, 4, 0, 0],
               [3, 0, 0, 1, 2],
               [0, 1, 0, 0, 2],
               [0, 0, 0, 0, 0],

               ]

    print(EdmondsKarp(matriz, matriz1, 0, 3))
