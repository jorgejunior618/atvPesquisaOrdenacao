from time import perf_counter
import numpy as np;
import matplotlib.pyplot as plotter;

############ DURAÇÃO DO MÉTODO ############
def medirTempo(funcao):
  inicio = perf_counter()
  funcao()
  fim = perf_counter()

  return (fim - inicio)

############ ARREDONDAMENTO DE FLOAT, COM CASA DECIMAL ############
def arredondar(num, dec=0):
  num = str(num)[:str(num).index('.')+dec+2]
  if num[-1]>='5':
      return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
  return float(num[:-1])


############ GERADOR DE LISTA ALEATÓRIA POR TAMANHO ############
def geraLista(quantidadeItens):
  lista = np.random.randint(0, quantidadeItens, quantidadeItens)
  novaLista = np.array(lista)
  return novaLista

def geraListaPiorCaso(quantidadeItens):
  # lista = np.random.randint(0, quantidadeItens, quantidadeItens)
  lista = np.random.randint(quantidadeItens, quantidadeItens*1000, quantidadeItens)
  novaLista = np.array(lista)
  return novaLista

############ MÉTODO DE ORDENAÇÃO ############
def countingSortForRadix(inputArray, placeValue):
    countArray = [0] * 10
    inputSize = len(inputArray)

    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[int(placeElement)] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[int(placeElement)] -= 1
        newPosition = countArray[int(placeElement)]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixsort(inputArray):
    maxEl = np.max(inputArray)

    index = 1
    while maxEl > 0:
        maxEl /= 10
        index += 1
    
    placeVal = 1

    outputArray = inputArray
    while index > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        index -= 1

    return outputArray

############ VARIÁVEIS E PROGRAMA ############

listasAleatorias = [
  geraLista(1000),
  geraLista(2000),
  geraLista(3000),
  geraLista(4000),
  geraLista(5000),
  geraLista(8000),
  geraLista(10000),

]

listasOrdenadas = []
listasPiorCaso = [
  geraListaPiorCaso(1000),
  geraListaPiorCaso(2000),
  geraListaPiorCaso(3000),
  geraListaPiorCaso(4000),
  geraListaPiorCaso(5000),
  geraListaPiorCaso(8000),
  geraListaPiorCaso(10000),
]

tamanhos = []
duracoesAleatorio = []
duracoesPiorCaso = []

print('listasAleatorias:')
for lista in listasAleatorias:
  print(lista)
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(radixsort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

print('listasOrdenadas:')
for lista in listasOrdenadas:
  print(lista)

# for lista in listasPiorCaso:
#   duracaoOrdenacao = medirTempo(
#     lambda : listasOrdenadas.append(radixsort(lista.copy()))
#   )
#   duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Radixsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
# plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
