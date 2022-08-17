from main import Pessoa
#p1 = Pessoa.por_ano_nascimento('Juan', 2002)
p1 = Pessoa('juan', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()