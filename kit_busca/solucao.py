class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    estado: str = None
    pai = None
    acao: str = None
    custo: int = None
    filhos = []

    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        # substitua a linha abaixo pelo seu codigo


# 1 2 3
# 4 5 6
# 7 8 9


dictAdjacencia = {
    1: {"abaixo": 4, "direita": 2},
    2: {"abaixo": 5, "esquerda": 1, "direita": 3},
    3: {"abaixo": 6, "esquerda": 2},
    4: {"abaixo": 7, "direita": 5, "acima": 1},
    5: {"abaixo": 8, "esquerda": 4, "direita": 6, "acima": 2},
    6: {"abaixo": 9, "esquerda": 5, "acima": 3},
    7: {"acima": 4, "direita": 8},
    8: {"acima": 5, "esquerda": 7, "direita": 9},
    9: {"acima": 6, "esquerda": 8},
}


def sucessor(estado: str):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    pos = estado.find("_")
    # 1 indexed
    adjacent = dictAdjacencia[pos + 1]
    results = []
    for action, newPosition in adjacent.items():
        # swap do '_' com a sua nova posição
        newState = list(estado)
        # newPosition é 1 indexado
        tmp = newState[newPosition - 1]
        newState[newPosition - 1] = "_"
        newState[pos] = tmp
        results.append((action, "".join(newState)))
    return results


def expande(nodo: Nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    return list(
        map(
            lambda tupla: Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1),
            sucessor(nodo.estado),
        )
    )


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
