from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

#fila_teste = filanormal()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#print(fila_teste.chamacliente(5))
#print(fila_teste.chamacliente(10))
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

#fila_teste2 = FilaNormal()
#fila_teste2.atualiza_fila()
#fila_teste2.atualiza_fila()
#fila_teste2.atualiza_fila()
#print(fila_teste2.chama_cliente(10))
#print(fila_teste2.chama_cliente(1))
#print(fila_teste2.estatistica('10/01/1994', 197, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('20/03/2025', 120)))
