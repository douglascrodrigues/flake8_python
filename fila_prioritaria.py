#pep-8, guia de estilo de códio, CONSISTENCIA!
"""
    Mypy - valida se estamos utilizando os tipos de dados corretos nas
    variaveis, parametros e retornos -> mypy nome_arquivo.py
"""

from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self)-> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int)-> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'\nCliente atual: {cliente_atual}, ') +  \
            (f'dirija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str)-> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            estatistica[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = (
                            len(self.clientes_atendidos))

        return estatistica
