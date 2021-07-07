# AD2 2017.1 - Questão 4
# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

#Subprogramas
def analisa():
    bd = open("arquivos_teste/hashtags.txt", "r")
    qtde = bd.readline()
    hashtags = {}
    maior = 0

    for i in range(int(qtde)): #Conta quantas vezes cada hashtag aparece
        linha = bd.readline()
        if hashtags.get(linha) == None:
            hashtags[linha] = 1
        else:
            valor = int(hashtags[linha])
            hashtags[linha] = valor + 1
    bd.close()

    for chave in hashtags:  #Verifica quais hashtags se repetem o maior número de vezes
        if int(hashtags[chave]) > maior:
            maior = hashtags[chave]
            trend = [chave]
        elif int(hashtags[chave]) == maior:
            trend.append(chave)
    trend.sort()

    return trend

def grava(trend):
    topics = open("trendtopics.txt", "w")
    for i in range(len(trend)):
        topics.write(trend[i])
    topics.close()
    return topics

#Programa Principal
trend = analisa()
topics = grava(trend)