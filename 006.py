#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um numero: "))

print('O numero que você digitou foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.0f}'.format(n,(n*2),(n*3),(n**(1/2))))

#nesse modo, usamos menos variaveis possiveis.
#no ultimo colchete usamos :;0f pra que não houvessem casas após o ponto.