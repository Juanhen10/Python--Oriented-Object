"""
public, protected, private]
_ = protected
__ = private
"""
class BasedeDados:
    def __init__(self):
        self.__dados = {}

    def inserit_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)
    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]

bd = BasedeDados()
bd.inserit_cliente(1, 'juan')
bd.inserit_cliente(2, 'Messi')
bd.lista_clientes()
print()
