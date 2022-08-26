# Métodos
lista = [1, 3, 12, 8, 2]
lista2 = [1, 2, 3]

print('Inicio: ', lista)

lista.append(3)
print('Append: ', lista)

lista.insert(2, 10)
print('Insert: ', lista)

lista.extend(lista2)
print('Extend: ', lista)

lista.pop()
print('Pop:    ', lista)

lista.pop(2)
print('Pop2:   ', lista)

lista.remove(3)
print('Remove: ', lista)
print('----')

print('Quantidade de 2 na Lista:      ', lista.count(2))
print('Index do elemento 12 na Lista: ', lista.index(12))
print('----')

lista.sort()
print('Sort:         ', lista)

lista.sort(reverse=True)
print('Sort Reverse: ', lista)
print('----')

# Funções
print('Len: ', len(lista))

print('Sum: ', sum(lista))

print('Min: ', min(lista))

print('Max: ', max(lista))