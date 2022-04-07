from random import randint


def criaItems(quantidade):

    listaItems = []
    for i in range (0, quantidade):
        valor = randint(1, 10)
        peso = randint(1, 10)
        item = {"id": i, "valor": valor, "peso": peso}
        listaItems.append(item)

    for j in range(0, len(listaItems)):
        print(listaItems[j])

    return listaItems

capacidade = 10

def constroiTabela(listaItems):
    tabela = []
    

    return tabela


def montaMochila(listaItems, capacidade):
    mochila = []
    maiorValor = 0
    capacidadeDisponivel = capacidade

    print("mochila")
    for item in listaItems:
        if item["valor"] > maiorValor:
            if item["peso"] <= capacidadeDisponivel:
                maiorValor = item["valor"]
                mochila.append(item)

        print(item)


    return mochila

listaItens = criaItems(10)
mochila = montaMochila(listaItens, capacidade)

print("Melhor mochila: ", mochila)