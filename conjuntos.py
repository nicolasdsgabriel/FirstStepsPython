# conjunto = {1, 2, 3, 4, 4, 2}
#
# conjunto.add(9) #add adiciona um valor ao conjunto
# conjunto.discard(1) #discard descarta um valor
# print(conjunto)

#---------------------------------------------------#

# conjunto = {5, 1, 2, 3}
# conjunto2 = {4, 5, 6}
#
# conjunto_uniao = conjunto.union(conjunto2) #union faz a união de dois conjuntos
# print('União: {}'.format(conjunto_uniao))
#
# conjunto_interseccao = conjunto.intersection(conjunto2)#intersection mostra os números iguais presentes nos conjuntos
# print('Intersecção: {}'.format(conjunto_interseccao))
#
# conjunto_diferenca = conjunto.difference(conjunto2) #difference mostra os valores que são diferentes presentes nos conjuntos
# print('Diferença: {}'.format(conjunto_diferenca))
#
# conjunto_difsim = conjunto.symmetric_difference(conjunto2)#difference é o que tem em um e não tem no outro, diferença simétrica () é a diferença presente nos dois nos dois
# print('Diferença simétrica: {}'.format(conjunto_difsim))

#-------------------------------------------------#

# conjuntoA = {1, 2, 3}
# conjuntoB = {1, 2, 3, 4, 5} #conjuntoB é um subconjunto de conjuntoA
#
# conjunto_subset = conjuntoA.issubset(conjuntoB)
# print('A é subconjunto de B? {}'.format(conjunto_subset))
#                                                                 #A é subconjunto de B porque B possui todos os valores do conjunto A, e A não é superconjunto de B porque não possui todos os valores do B
# conjunto_superset = conjuntoA.issuperset(conjuntoB)
# print('A é super conjunto de B? {}'.format(conjunto_superset))

#--------------------------------------------------#

# lista = ['cachorro', 'gato', 'cachorro']
# print(lista)
#
# conjunto_animal = set(lista) #set faz a conversão de algo para conjunto (assim como o list e o tuple)
# print(conjunto_animal)
# #a conversão da lista faz as duplicidades sumirem
#
# lista_animais = list(conjunto_animal)
# print(lista_animais)
# #convertendo para lista de novo as duplicidades continuam inexistentes

