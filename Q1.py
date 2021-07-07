# AD2 2017.1 - Questão 1
# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

# Operações
def car(lis):
    return lis[0]

def cdr(lis):
    return lis[1:]

def cons(x, lis):
    return [x]+lis

def ehLista(x):
    return isinstance(x, list)

def ehAtomo(x):
    return not ehLista(x)

#Subprogramas Auxiliares
def ordenar(lista):  #ordena uma lista
    if lista == []:
        return []
    else:
        return insereOrdenado(car(lista), ordenar(cdr(lista)))

def insereOrdenado(x, lista): #insere um elemento da lista de forma ordenada
    if lista == [] or x < car(lista):
        return cons(x, lista)
    else:
        return cons(car(lista), insereOrdenado(x, cdr(lista)))

def elementoFinal(lista): #retorna último elemento de uma lista
    if lista == []:
        return None
    else:
        if cdr(lista) == []:
            return car(lista)
        else:
            return elementoFinal(cdr(lista))

def retiraNegativos(lista): #retira da lista os números menores
    if lista == []:
        return None
    else:
        if car(ordenar(lista)) == [] or car(ordenar(lista)) > 0:
            return lista
        else:
            return retiraNegativos(cdr(ordenar(lista)))

def soma(lista):
    if lista == []:
        return 0
    else:
        if ehAtomo(car(lista)):
            return car(lista) + soma(cdr(lista))
        else:
            return soma(car(lista)) + soma(cdr(lista))

def somaPositivos(lista):
    if lista == []:
        return 0
    else:
        return (soma(retiraNegativos(lista)))

#Subprogramas

def maior(lista):
    if lista == []:
        return 0
    else:
        return elementoFinal(ordenar(lista)) #retorna o último elemento de uma lista ordenada

def mediaPositivos(lista):
    if lista == []:
        return 0
    else:
        if elementoFinal(ordenar(lista)) <= 0 :  #se último elemento da lista ordenada for igual a zero ou negativo, retornar 0
            return 0
        else:
            return somaPositivos(lista) / len(retiraNegativos(lista)) #soma números positivos da lista e divide pela quantidade de nºs positivos

def emagrece(lista):
    if lista == []:
        return []
    else:
        if ehAtomo(car(lista)):
            return cons(car(lista), emagrece(cdr(lista)))
        else:
            return emagrece(car(lista)) + emagrece(cdr(lista))

# Programa Principal

#Entradas
dadosTeste1 = [10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, -99, 12, 17]
dadosTeste2 = []
dadosTeste3 = [-10, -13, 12.99, 100, 888, 0, 83]
dadosTeste4 = [-10, -2, -5, 13, -26, -4, 3, -9, 33, -18, -6, -99, -12, 17]
dadosTeste5 = [-10, -2, -5]
dadosTeste6 = [[[]]]
dadosTeste7 = ["ana", [["maria", "chico"]], [[["igor"]]], "juca"]
dadosTeste8 = [10, 2, 5, 13, [[[26, [[4]], 2]]], 9, 33, [18, 6], 99, 12, 17]

#Saídas
print(maior(dadosTeste1))
print(maior(dadosTeste2))
print(maior(dadosTeste3))
print()
print(mediaPositivos(dadosTeste4))
print(mediaPositivos(dadosTeste2))
print(mediaPositivos(dadosTeste5))
print()
print(emagrece(dadosTeste2))
print(emagrece(dadosTeste6))
print(emagrece(dadosTeste7))
print(emagrece(dadosTeste8))