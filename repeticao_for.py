for i in range(10):
  print(i)
print('---')

for i in range(5, 10):
  print(i)
print('---')

for i in range(5, 10, 2):
  print(i)
print('---')

soma = 0
for i in range(1, 4):
  nota = float(input(f'Informe a nota {i}: '))
  soma = soma + nota
  
media = soma / 3
print(f'A media é: {media}')