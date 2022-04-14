from random import choice, random

target = '1001'
genes = '01'
tamPopulacao = 10

generation = 1 #geracao atual
encontrou = False
populacao = ['1000', '1111', '1010', '0001', '1110', '0000', '1011', '0101', '1100', '1101']

def mutacao():
    gene = choice(genes)
    return gene

def sexo(pai, mae):

    prob = random()
    filho = ''

    for genePai, geneMae in zip(pai, mae):
            if prob < 0.45:
                filho += genePai
                # if prob is between 0.45 and 0.90, insert
                # gene from parent 2
            elif prob < 0.90:
                filho += geneMae
                 # otherwise insert random gene(mutate),
                # for maintaining diversity
            else:
                filho += mutacao()

    return filho

while not encontrou:

    for individuo in populacao:
        if individuo == target:
            print(individuo)
            break

    novaGeracao = []
    elite = int(tamPopulacao * 0.1) #apenas 10% (elite) vao para a proxima geracao
    novaGeracao.extend(populacao[:elite])

    #Os 50% mais adequados (fittest) vao reproduzir 
    resto = int(tamPopulacao * 0.9)

    for _ in range(resto):
        pai = choice(populacao[:50])
        mae = choice(populacao[:50])
        filho = sexo(pai, mae)
        print(pai, "x", mae, "=", filho)

