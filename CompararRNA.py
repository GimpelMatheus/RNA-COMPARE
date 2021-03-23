
entradaBacteria = open("bacteria.fasta").read()
saidaBacteria = open("bateria.html", "w")


entradaHumanos = open("human.fasta").read()
saidaHumanos = open("humano.html", "w")


contagem = dict()

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		contagem[i + j] = 0


for k in range(len(entradaBacteria) - 1):
	contagem[entradaBacteria[k] + entradaBacteria[k+1]] += 1

#HTML

i = 1 #contador i
j = max(contagem.values())

for k in contagem:

	transparencia = contagem[k]/j
	saidaBacteria.write("<div style = 'width: 100px; border: 1px solid #111; height: 100px; float:left; background-color: rgba(0,0,0, " + str(transparencia) +")'>" + k + "</div>")

	if i % 4 == 0:
		saidaBacteria.write("<div style = 'clear: both' </div>")

	i += 1


saidaBacteria.close()

#HUMANO

contagem = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		contagem[i + j] = 0

entradaHumanos = entradaHumanos.replace("\n", "")

for k in range(len(entradaHumanos) - 1):
	contagem[entradaHumanos[k] + entradaHumanos[k+1]] += 1

#HTML

i = 1 #contador i
j = max(contagem.values())

for k in contagem:

	transparencia = contagem[k]/j
	saidaHumanos.write("<div style = 'width: 100px; border: 1px solid #111; height: 100px; float:left; background-color: rgba(0,0,0, " + str(transparencia) +")'> " + k + "</div>")

	if i % 4 == 0:
		saidaHumanos.write("<div style = 'clear: both' </div>")

	i += 1


saidaHumanos.close()
