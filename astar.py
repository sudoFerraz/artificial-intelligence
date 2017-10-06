import collections


class Grafo:
	def __init__(self):
		self.nos = []

	def get_nos(self):
		return self.nos

	def put_no(self, no):
		self.nos.append(no)

class no:
	def __init__(self, nome):
		self.direita = None
		self.esquerda = None
		self.aspira = None
		self.arestas = [self.direita, self.esquerda, self.aspira]
		self.final = False
		self.nome = nome
		self.custo = 1

	def set_meta(self):
		self.final = True


	def put_arestas(self, no_direita, no_esquerda, no_aspira):
		self.direita = no_direita
		self.esquerda = no_esquerda
		self.aspira = no_aspira

grafo = Grafo()
#no inicial comeca na direita com os dois comodos sujos 
estado_inicial_s0 = no("s0")
s1 = no("s1")
s2 = no("s2")
s3_final = no("s3")
s3_final.set_meta()
s4 = no("s4")
s5 = no("s5")
s6_final = no("s6")
s6_final.set_meta()
s7 = no("s7")

estado_inicial_s0.put_arestas(estado_inicial_s0, s4, s1)
s1.put_arestas(s1, s5, s1)
s2.put_arestas(s2, s7, s3_final)
s3_final.put_arestas(s3_final, s6_final, s3_final)
s4.put_arestas(estado_inicial_s0, s4, s7)
s5.put_arestas(s1, s5, s6_final)
s6_final.put_arestas(s3_final, s6_final, s6_final)
s7.put_arestas(s2, s7, s7)

grafo.put_no(estado_inicial_s0)
grafo.put_no(s1)
grafo.put_no(s2)
grafo.put_no(s3_final)
grafo.put_no(s4)
grafo.put_no(s5)
grafo.put_no(s6_final)
grafo.put_no(s7)


custo_caminhos = {}
custo_caminho = 0
already_visited = []
fila_prioridade = []
fila_prioridades = []

global globfound
globfound = False

def eh_vazio(lista):
	if len(lista) == 0:
		return True
	else:
		return False



nos = grafo.get_nos()

def astar_search(no):
	already_visited.append(no)
	fila_prioridades.append(no.arestas)
	print no.arestas
	for sublist in fila_prioridades:
		for item in sublist:
			fila_prioridade.append(item)
	print fila_prioridade

	while not eh_vazio(fila_prioridade):
		no = fila_prioridade.pop()
		if no.final == True:
			print "achou"
			print custo_caminho
			return no
		else:
			custo_caminho = custo_caminho + no.custo
			astar_search(no)

astar_search(estado_inicial_s0)








#tabela de estados >
#s0 -> aspirador na direita, direita suja, esquerda suja
#s1 -> aspirador na direita, direita limpa, esquerda suja
#s2 -> aspirador na direita, direita suja, esquerda limpa
#s3 -> aspirador na direita, direita limpa, esquerda limpa -> final
#s4 -> aspirador na esquerda, direita suja, esquerda suja
#s5 -> aspirador na esquerda, direita limpa, esquerda suja
#s6 -> aspirador na esquerda, direita limpa, esquerda limpa -> final
#s7 -: aspirador na esquerda, direita suja, esquerda limpa
