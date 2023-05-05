#Exemplo>>  a: int = 0
#typehint  é apenas uma dica para mostrar ao dev o tipo de dados que
#uma determinada variavel deve aceitar, mais não bloqueia se você
#colocar uma dado diferente do solicitado

from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualiza_fila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clintesatendidos.append(cliente_atual)
        #Template string
        return (f'\nCliente atual: {cliente_atual},') + \
            ('dirija-se ao caixa: {caixa} ')
