import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    """
        Classe abstrata não herda nada da classe mae, porem,
        obriga as classes filhas a herda-la, ou seja, quem
        HERDAR ou INSTANCIAR a classe mae e obrigado a utilizar esses
        metodos criados.
    """

    @abc.abstractclassmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractclassmethod
    def chama_cliente(self, caixa: int):
        ...
