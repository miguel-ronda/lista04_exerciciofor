#010 - Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
print(" miguel do amaaral paes ronda")
quanti=int(input("quantas pessoas voce ira convidar"))
if quanti <= 10:
    for i in range (quanti):
        nome = (input("digite o nome do convidado"))
        print(quanti,"esta convidados para festa")
else:
    print("voce convidou muitas pessoas")        
