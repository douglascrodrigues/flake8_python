#Exemplo>>  a: int = 0
#typehint  é apenas uma dica para mostrar ao dev o tipo de dados que
#uma determinada variavel deve aceitar, mais não bloqueia se você
#colocar uma dado diferente do solicitado

class FilaNormal:
    codigo: int = 0
    fila = []
    clintesatendidos = []
    senhaatual: str = ""

    def gerasenhaatual(self)-> None:
        self.senhaatual = f'NM{self.codigo}'

    def resetafila(self)-> None:
        if self.codigo >= 100:
            self.codigo=0
        else:
            self.codigo += 1

    def atualizafila(self)-> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa: int)-> str:
        cliente_atual: str = self.fila.pop(0)
        self.clintesatendidos.append(cliente_atual)
        #Template string
        return(f'\nCliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')