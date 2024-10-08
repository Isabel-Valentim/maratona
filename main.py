import math

def converterCoordenadas(lista):
    for i in range(len(lista)):
        lista[i] = [int(str(lista[i]).split(' ')[0]), int(str(lista[i]).split(' ')[1])]
    return lista
        
# armazenar as entradas
coordenadas = []
pontosMedios = []
resultado = []
#coletar entrada de quantidade de numeros
while True:
    tamanho = int(input('tamanho: '))
    if(tamanho >= 1 and tamanho <=100):
        #coletar entrada das coordenadas
        while (len(coordenadas) < tamanho):
            coordenada = input('coordenada: ')
            if coordenada == 0:
                break
            else:
                coordenadas.append(coordenada)
        break

listaCoordenadas = converterCoordenadas(coordenadas)
for cont, coordenada in enumerate(listaCoordenadas):
    coordenadaA = listaCoordenadas[cont]
    listaApermutar = listaCoordenadas[cont+1:]
    for cont, coordenada in enumerate(listaApermutar):
        coordenadaB = listaApermutar[cont]
        # calcular todos os pontos médios possíveis
        pontoMedioX = (coordenadaA[0]+coordenadaB[0])/2
        pontoMedioY = (coordenadaA[1]+coordenadaB[1])/2
        pontoMedio = [pontoMedioX, pontoMedioY]
        if pontoMedio not in pontosMedios: 
            pontosMedios.append(pontoMedio)
    #para cada coordenada calcular a distância de todos os pontos médios possíveis
    for pm in pontosMedios:
        distancia = math.sqrt((((pm[0] - coordenadaA[0])**2) + ((pm[1] - coordenadaA[1])**2)))
        resultado.append([coordenadaA, pm, distancia])

print(resultado)
# verificar se coordenadas com o mesmo ponto do meio tem a mesma distancia
for count,e in enumerate(resultado):
    coordenada = e[0]
    pontoMedio = e[1]
    raio = e[2]
    
