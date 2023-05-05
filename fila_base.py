import abc
from typing import List
#import de funcoes e classes built-in

#import de classe do projeto, pula 1 linha
from constantes import TAMANHO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
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

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...
    """
        Template Method - Pra que criar um metodo igual que
        faz as mesmas coisas em classes diferentes, porém,
        que herdam ou instacia a classe mae , se pode se
        criar na propria classe mae e chama-la independente da heranca?
    """

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    #@abc.abstractmethod
    #def estatistica(self, dia, agencia, flag_detail):
    #    ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...
