#Exemplo>>  a: int = 0
#typehint  é apenas uma dica para mostrar ao dev o tipo de dados que
#uma determinada variavel deve aceitar, mais não bloqueia se você
#colocar uma dado diferente do solicitado

from fila_base import FilaBase
from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    def gera_senha_atual(self)-> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        #Template string
        return (f'\nCliente atual: {cliente_atual}, ') + \
            (f'dirija-se ao caixa: {caixa} ')
