"""
    Trabalho da disciplina de Linguagens Formais e Autômatos (2020/1)

 Tema: Implementação de um programa Python para ler a definição de um AFN M e 
 uma palavra w e responder se w pertence a L(M).
"""
# -*- coding: utf-8 -*-

a = "M=({0,1}, {1,2}, {(1,a,1), (1,b,1), (1,ε,2)}, 1, {2})"

print("\nLISTA NORMAL:")
print(a)
b = a.split("},")
elementosFinais = b[3].split(", ")
b.pop()
b.append(elementosFinais[0])
b.append(elementosFinais[1])
print("\nLISTA SEPARADA:")
print(b)
print("\nREMOVENDO ESPAÇOS NO INICIO E FIM DE CADA STRING:")
for i in range(0, len(b)):#for el in b:
    b[i] = b[i].strip()
print("\nLISTA FINAL:")
print(b)


""" #Teste com XML

import xml.etree.ElementTree as ET
tree = ET.parse('items2.xml') # Tomar cuidado com o local do arquivo
root = tree.getroot()

# one specific item attribute
print('Item #2 attribute:')
print(root[1][1].attrib)

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')
print(root[0][1].text)

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)

"""