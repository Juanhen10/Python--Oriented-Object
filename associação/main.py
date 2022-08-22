from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escrito = Escritor('juyan')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

escrito.ferramenta = maquina
escrito.ferramenta.escrever()
