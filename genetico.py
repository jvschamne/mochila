from random import choice, random
from time import sleep

target = '1001'
genes = '01'
tamPopulacao = 10

generation = 1 #geracao atual
encontrou = False
populacao = ['1000', '1111', '1010', '0001', '1110', '0000', '1011', '0101', '1100', '1101']

def funcaoFitness(populacao):
    """
        calcula a pontuacao fitness dos indiviuos e os ordena de acordo com ela
        a pontuacao fitness eh a quantidade de chars diferentes do target
    """
    
    populacaoFitness = []
    vetorFitness = []

    #calcula o fitness de cada individuo
    for individuo in populacao:
        fitness = 0
        for charIndividuo, charTarget in zip(individuo, target):
            if charIndividuo != charTarget:
               fitness += 1

        aux = {'individuo': individuo, "fitness": fitness}
        populacaoFitness.append(aux)
        vetorFitness.append(fitness)

    #ordena os individuos
    vetorFitness.sort()
    print(vetorFitness)

    index = 0 
    while(len(populacaoFitness) > 0):
        for pop in populacaoFitness:
            if vetorFitness[index] == pop["fitness"]:
                populacao[index] = pop["individuo"]
                populacaoFitness.remove(pop)
                index +=1
                break

    print(populacao)

    return populacao


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
    print("GERACAO", generation)
    generation += 1

    populacao = funcaoFitness(populacao)

    print(populacao[0])
    if populacao[0] == target:
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
        novaGeracao.append(filho)

    populacao = novaGeracao

