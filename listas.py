notas = [7.9, 9.7, 8.2]

lista = []
lista = list()
lista = [26, 2.6, 'Oi', 2, 78, True]

list_of_list = [[0,1], [0,1]]

print(lista[1])
print(lista[-1])
print(lista[1:4])
print(lista[3:])
print(lista[2:6:2])
print('----')

for e in lista:
  print(e)
print('----')

for i in range(len(lista)):
  print(i)
print('----')

print(f'Comprimento da lista: {len(lista)}')