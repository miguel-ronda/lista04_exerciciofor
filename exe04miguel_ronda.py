#4-escreva um programa para pedir um numero e em seguida o nome. exiba o nome (uma letra de cada vez, em cada linha) e repita isso para o numero de vezes digitado
print("miguel do amaral paes ronda")
num=int(input("DIGITE UM NUMERO: "))
nome=(input("insira seu nome: "))
for i in range (num):
    for letra in nome:
        print(letra)