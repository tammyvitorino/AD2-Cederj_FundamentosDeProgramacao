# AD2 2017.1 - Questão 3
# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

#Subprogramas
def criaAgenda():
    agenda = dict()
    lista = []
    entrada = input("Informe nome e telefone:").split()
    while entrada[0] != "acabou":
        lista.append([entrada[1], entrada[0]])
        agenda[entrada[0]] = entrada[1]
        entrada = input().split()
    return agenda, lista

def saidas(nomes, numeros):
    for chave in sorted(nomes):
        print(chave, agenda.get(chave))
    print()
    for i in range(len(numeros)):
        print(numeros[i][1], numeros[i][0])
    return None

#Programa Principal
agenda, nomes_agenda = criaAgenda()
nomes_agenda.sort()
saidas(agenda, nomes_agenda)