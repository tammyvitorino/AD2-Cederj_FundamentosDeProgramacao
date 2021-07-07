# AD2 2017.1 - Questão 5
# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

#Subprogramas
def geraMatriz():  #recebe as entradas das matrizes A e B e gera as matrizes esparsas de ambas
    tamanhoMatriz = input().split()
    linhas = int(tamanhoMatriz[0])
    colunas = int(tamanhoMatriz[1])
    matrizEsparsa = {}

    for i in range(linhas):
        linhaMatriz = input().split()
        for j in range(len(linhaMatriz)):
            if int(linhaMatriz[j]) != 0:
                matrizEsparsa[(i,j)] = int(linhaMatriz[j])

    return matrizEsparsa, tamanhoMatriz

def multiplicaMatrizes(a,b,tA,tB): #gera a matriz esparsa da multiplicação entre A e B
    m, n = int(tB[1]), int(tA[0])
    t = int(tA[1])
    matrizFinal = {}

    for i in range(m):
        for j in range(n):
            valor = 0
            for k in range(t):
                if ((a.get((i,k))) != None) and ((b.get((k,j)))) != None:
                     valor = valor + ((a[(i,k)] * b[(k,j)]))
                if valor != 0:
                    matrizFinal[(i, j)] = valor

    return matrizFinal

def imprimeMatrizes(a,b,r):
    print("Matriz esparsa A")
    print(a)
    print()
    print("Matriz esparsa B")
    print(b)
    print()
    print("Matriz esparsa R")
    print(r)
    return None


#Programa Principal
matrizA, tamanhoA =  geraMatriz()
matrizB, tamanhoB =  geraMatriz()
matrizR = multiplicaMatrizes(matrizA, matrizB, tamanhoA, tamanhoB)
imprimeMatrizes(matrizA, matrizB, matrizR)

