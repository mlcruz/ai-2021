import collections
import heapq


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    estado: str = None
    pai = None
    acao: str = None
    custo: int = None

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

    # implementamos um comparador qualquer de nodos para minHeap
    # A comparação não tem semantica definida, mas precisa existir
    def __lt__(self, other):
        return False


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
    expandido = []

    for acao, estado in sucessor(nodo.estado):
        expandido.append(Nodo(estado, nodo, acao, nodo.custo + 1))

    return expandido


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    fronteira = Fila()
    return busca_generica(estado, fronteira)


def caminho(nodo: Nodo):
    """
    Computa o caminho de um nodo expandindos todos seus pais
    """
    caminho = collections.deque()
    caminho.appendleft(nodo.acao)
    atual = nodo.pai
    while atual is not None:
        if atual.acao is not None:
            caminho.appendleft(atual.acao)
        atual = atual.pai
    return caminho


class Fila(collections.deque):
    def take(self):
        return self.popleft()

    def add(self, nodo: Nodo):
        return self.append(nodo)


class Pilha(collections.deque):
    def take(self):
        return self.pop()

    def add(self, nodo: Nodo):
        return self.append(nodo)


class Hamming:
    # minheap como fila de prioridae
    __heap: list

    def __init__(self):
        self.__heap = []

    def __len__(self):
        return len(self.__heap)

    def add(self, nodo: Nodo):
        # distancia de hemming do estado final
        distancia = 0
        for i, char in enumerate(nodo.estado):
            expected = str(i + 1)
            # se é _, compara corretamente
            if i == 8:
                expected = "_"

            if char != expected:
                distancia += 1

        # Peso, Valor para minheap
        return heapq.heappush(self.__heap, (distancia + nodo.custo, nodo))

    def take(self):
        # minheap mantem order no pop
        nodo = heapq.heappop(self.__heap)
        # sem o peso
        return nodo[1]


def busca_generica(estado, fronteira):
    """
    Implementa a busca generica utilizando uma estrutura e dados (fila etc)
    recebida como parametro
    """
    explorados = set()
    estadosFronteira = set()
    inicio = Nodo(estado, None, None, 0)
    fronteira.add(inicio)
    contagemExpandido = 0

    while True:
        if len(fronteira) == 0:
            return None
        v: Nodo = fronteira.take()
        contagemExpandido += 1
        if v.estado == "12345678_":
            print(f"{v.custo} - {contagemExpandido}")
            return caminho(v)
        if v.estado not in explorados:
            explorados.add(v.estado)
            for expandido in expande(v):
                if (
                    expandido.estado not in estadosFronteira
                    and expandido.estado not in explorados
                ):
                    fronteira.add(expandido)
                    estadosFronteira.add(expandido.estado)


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
    fronteira = Pilha()
    return busca_generica(estado, fronteira)


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
    fronteira = Hamming()
    return busca_generica(estado, fronteira)


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
