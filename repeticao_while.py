n1 = 15

n_escolhido = int(input('Escolha um número: '))

while n1 != n_escolhido:
  print('Você perdeu')
  n_escolhido = int(input('Escolha um número: '))
  
print('Você ganhou')


contador = 0
while contador < 5:
  print(contador)
  contador = contador + 1