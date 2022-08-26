dicionario = {}
dicionario = dict()
dicionario = { 'nome': 'Victor', 'idade': 24, 'altura': 1.72 }

print(dicionario)
print(dicionario['nome'])

dicionario['programador'] = True
print(dicionario)
print('---')

for chave in dicionario:
  print(chave, '-', dicionario[chave])
print('---')

print('peso' in dicionario)
print('altura' in dicionario)