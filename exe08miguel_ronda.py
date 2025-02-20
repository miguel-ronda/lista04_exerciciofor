#8-defina uma variável chamada "total" com o valor 0. 
# peca ao usuário apara inserir 5 numero e, após cada entrada pergunte se ele deseja que este numero seja incluído ("S-s", "N-n"),
#  se ele desejar adicione o numero ao total, se ele não quiser inclui-lo não atribua, depois de exibir os cinco números exiba o total
print("miguel do amaral paes ronda")
total = 0
for i in range(5):
    num=int(input("DIGITE o {} NUMERO: ".format(i+1)))
    incluir = (input("deseja incluir esse numero? ").upper())
    if incluir.lower() =="s":
        total+= num
        print("o total sera de: ",total)


