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

############ MÉTODO DE ORDENAÇÃO ############
def quicksort(lista):
  tamanhoLista = len(lista)
  quick(lista, 0, tamanhoLista -1)
  return lista

def quick(lista, inicio, fim):
    tamanho = fim - inicio + 1
    listaAux = [0] * (tamanho)
 
    topo = 0
    listaAux[topo] = inicio
 
    topo = topo + 1
    listaAux[topo] = fim
 
    while (topo >= 0):
 
        fim = listaAux[topo]
        topo = topo - 1
        inicio = listaAux[topo]
        topo = topo - 1
 
        elementoPivo = particao(lista, inicio, fim)
 
        if elementoPivo - 1 > inicio:
            topo = topo + 1
            listaAux[topo] = inicio
            topo = topo + 1
            listaAux[topo] = elementoPivo - 1
 
        if elementoPivo + 1 < fim:
            topo = topo + 1
            listaAux[topo] = elementoPivo + 1
            topo = topo + 1
            listaAux[topo] = fim

def particao(lista, inicio, fim):
  esquerda = inicio - 1
  ultimo = lista[fim]

  for j in range(inicio, fim):
    if (lista[j] <= ultimo):
      esquerda = esquerda + 1
      lista[esquerda], lista[j] = lista[j], lista[esquerda]

  lista[esquerda + 1], lista[fim] = lista[fim], lista[esquerda + 1]
  return esquerda + 1


############ VARIÁVEIS E PROGRAMA ############

listasAleatorias = [
  geraLista(10000),
  geraLista(20000),
  geraLista(30000),
  geraLista(40000),
  geraLista(50000),
  geraLista(80000),
  geraLista(110000),
  geraLista(150000)
]

listasOrdenadas = []
listasPiorCaso = []

tamanhos = []
duracoesAleatorio = []
duracoesPiorCaso = []

for lista in listasAleatorias:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(quicksort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])

for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(quicksort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Selectionsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
