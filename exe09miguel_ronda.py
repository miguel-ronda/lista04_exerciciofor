#9- faca um programa que pergunte em qual direção o usuário deseja apontar, para cima C\c, para baixo A\a,
#  se ele selecionar para cima, peça um numero superior a 20  e conte de um ate este numero, se ele selecionar para baixo, peça um numero 
#abaixo de vinte, em seguida, faça contagem regressiva de 20 ate este numero. se ele selecionar algo diferente, exiba a mensagem "direção invalida".
print("miguel do amaral paes ronda")
direct=input("qual direcao voce quer seguir:")
if direct == "C":
    for i in range(1, int(input("digite um numero superior:"))+1):
        print(i)
elif direct == "A":
    numero= int(input("digite um numero abaixo de 20: "))  
    if numero<=20:      
        for i in range(20, numero -1,-1):
            print(i)
        else:
            print("numero invalido")
    else:
        print("direcao errada")           
