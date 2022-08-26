idade = 12

if idade >= 18:
  print('Você é maior de idade.')
else:
  print('Você é menor de idade.')


media = float(input('Digite a media: '))
presenca = int(input('Digite a presença: '))

if media >= 7 and presenca >= 70:
  print('Você passou.')
elif media >= 4 and presenca >= 70:
  print('Você está de recuperação.')
else:
  print('Você reprovou.')


if idade >= 18 or media >= 7:
  print('Pode jogar.')