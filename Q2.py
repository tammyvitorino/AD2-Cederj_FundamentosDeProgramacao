# AD2 2017.1 - Questão 2
# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

#ProgramaPrincipal
entrada = input("Entre com nome do arquivo a ser analisado")
bd = open(entrada, "r")
linha = bd.readline()
itens, soma, maior, media = 0, 0, 0, 0

if linha == "":
    bd.close()
    print("arquivo vazio")
else:
    while linha != "":
        numeros = linha.split()
        for i in numeros:
            itens = itens + 1
            soma = soma + float(i)
            if float(i) > maior:
                maior = float(i)
        linha = bd.readline()
    print ("Maior =", "%1.2f" % maior)
    print ("Menor =", "%1.2f" % (soma / itens))

bd.close()
