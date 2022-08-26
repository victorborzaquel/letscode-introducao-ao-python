def saudacao(nome, curso='Python'):
  print(f'Seja bem vindo {nome}!')
  print(f'Bem vindo ao curso de {curso}!')
  print('----')

saudacao('Victor')
saudacao('Hugo', 'Java')


def soma(n1, n2):
  return n1 + n2

resultado = soma(10, 5)
print('O resultado é:', resultado)