import sys #Para ler os argumentos da linha de comando
import re #Para verificar se o nome do arquivo é válido
from functions import * #Funcoes implementadas

def main(argv):
    

	#Bloco testando se os parametros contem algum erro
	try:
		fileName = argv[0]
		word = argv[1]

		#Testa se o fileName é válido utilizando essa expressao regualar
		pattern = re.compile(r'^[/\w,\s-]+\.xml$')
		match = pattern.search(fileName)    

		if match:
		    
			#Cria o automato
			af = createAutFromXML(fileName)

			#Cria o grafo que representa o automato
			graph = createGraph(af)

			#Palavra a ser processada
			word = sys.argv[2]

			initialState = str(af['q'][0].firstChild.data)

			#Lista contendo todas as arestas do grafo
			edges = graph.edges.data()

			print(Pe(initialState, word, edges, af))

		else:

			print("Arquivo não é xml ou não está especificado corretamente")

	except:
		print("Parametros com problema ! ")
    
if __name__ == "__main__":
   main(sys.argv[1:])    