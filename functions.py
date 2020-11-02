from xml.dom import minidom #Biblioteca com os recursos para ler o arquivo xml
import networkx as nx #Biblioteca com os recursos para montar um multigrafo direcionado

#Le devidamente o arquivo xml que contem a definição do automato
#Recebe o nome do arquivo como parametro
#Retorna o dicionário que representa o automato descrito pelo arquivo
def createAutFromXML(fileName):
    
    xmldoc = minidom.parse(fileName)
    
    #Divide cada tag do xml por propriedade do automato
    alphabet = xmldoc.getElementsByTagName('simbol')
    Q = xmldoc.getElementsByTagName('state')
    P = xmldoc.getElementsByTagName('transition')
    q = xmldoc.getElementsByTagName('initialState')
    F = xmldoc.getElementsByTagName('finalState')
    
    #Dicionário que representa automato com cada elemento de sua 5-upla 
    af = {}
    af['alphabet'] = alphabet
    af['Q'] = Q
    af['P'] = P
    af['q'] = q
    af['F'] = F
    
    return af

#Cria o grafo que representa o autamato
#Recebe o dicionário que representa o automato
#Retorna o grafo criado
def createGraph(af):
    
    #Criacao do multigrafo
    graph = nx.MultiDiGraph()

    #Lista que ira conter cada tupla que descreve uma aresta
    edges = []
    for transition in af['P']:
        simbols = transition.firstChild.data.split(",")
        edges.append(tuple(simbols))

    #Adiciona as arestas no grafo
    graph.add_weighted_edges_from(edges) 
    
    return graph


#Funcao Programa do automato
#Recebe uma lista de estados, um caracter e uma lista com as arestas do grafo
#Retorna uma lista de estados alcançáveis a partir da lista recebida
def funcaoP(states, caracter, edges):
    
    #Conjunto que representará o conjunto de estados a ser retornado
    statesSet = set()
    
    #Lista que contém as arestas que saem daquele estado, ou seja, as transições possíveis a partir dele
    stateEdges = []
    
    #Para cada estado, preenche a lista com as arestas (transições) que saem de cada um
    for state in states:
        for edge in edges:
            if edge[0] is state:
                stateEdges.append(edge)
    
    #Para cada aresta, testa se a transição é válida, ou seja, consome o símbolo. Preenche o conjunto de estados a ser retornado
    for edge in stateEdges:
        if edge[2]['weight'] is caracter:
            statesSet.add(edge[1])
                
                
    return statesSet

#Funcao Programa Estendida do automato
#Recebe um estado de partida ,uma palavra a ser processada, uma lista com as arestas do grafo,  e o automato correspondente
#Retorna se a palavra é ou não descrita pelo autômato
def Pe(state, word, edges, af):
    
    print("\nTesting if the word '" + word + "' is accepted by the finite automaton")
    
    states = set()
    states.add(state)
    
    #Preenche a lista que representará o conjunto de estados finais
    finalStates = set()
    for state in af['F']:
        finalStates.add(str(state.firstChild.data))
    
    #Se a palavra nao for vazia, processa-a
    if word:
        #Para cada caracter na palavra, chama a funcao programa passando o conjunto de estados correspondente e o caracter
        for caracter in word:
            states = funcaoP(states, caracter, edges)
    
    #Se o conjunto de estados não for vazio, testa se algum dos estados retornados esta no conjunto de estados finais
    if states:      
        for state in states:
            if state in finalStates:
                return ("ESTA NA LINGUAGEM")
    
    return ("NAO ESTA NA LINGUAGEM")