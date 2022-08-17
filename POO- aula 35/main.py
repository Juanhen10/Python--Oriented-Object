from pessoa import Pessoa
p1 = Pessoa('Juan',18)
p2 = Pessoa('Victor', 20)

p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())