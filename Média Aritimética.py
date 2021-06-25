import math
n1 = float(input('Digte a nota 1'))
n2= float(input('Digite a nota 2'))
n3 = float(input('Digite a nota 3'))
me = float(input('Digite a nota dos exercicios'))

ma = (n1+n2*2+n3*3+me)/7
print('a nota final é de{: .2f}'.format(math.ceil(ma)))
if ma >= 6:
   print('Está aprovado!')
else:
   print('Está reprovado!')


