#7-PEÇA AO USUARIO para inserir o seu nome e um numero, se o numero for menor doque 10, exiba o nome dele esse numero de vezes, caso contrario exibir a mensagem "numero muito alto " 3 vezes
print("miguel do amaral paes ronda")
num = int(input("DIGITE UM NUMERO: "))
nom= (input("difgite seu nome: "))
if num < 10 :
    for i in range (num):
        print(nom)
else:
        for i in range (3):
         print("numero muito alto")