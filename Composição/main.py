from   classes import Cliente, Endereco

cliente1 = Cliente('juan', 20)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('MAria', 55)
cliente2.insere_endereco('Salvado','BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_endereco()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Belo Horizonte', 'MG')
print(cliente3.nome)
cliente3.lista_endereco()

print('###############' * 10)