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
  novaLista = np.array(lista, dtype=int)
  return novaLista

# def geraListaPiorCaso(quantidadeItens):
#   lista = np.random.randint(low=quantidadeItens*9, high=quantidadeItens*10, size=quantidadeItens)
#   novaLista = np.array(lista, dtype=int)
#   return novaLista

############ VERIFICA SE OS ITENS DA LISTA SÃO IGUAIS ############
def listaDeRepetidos(lista):
  primeiro = lista[0]
  for item in lista:
    if item != primeiro:
      return False
  return True
            

############ MÉTODO DE ORDENAÇÃO ############
def bucketsort(lista):
  tamanhoLista = len(lista)
  buckets = [[], []]

  for i in range(tamanhoLista):
    if (lista[i] <= (np.max(lista) + np.min(lista)) / 2):
      buckets[0].append(lista[i])
    else:
      buckets[1].append(lista[i])
  
  if(len(buckets[0]) > 1 and
  not listaDeRepetidos(buckets[0])):
    buckets[0] = bucketsort(buckets[0])

  if(len(buckets[1]) > 1 and
  not listaDeRepetidos(buckets[1])):
    buckets[1] = bucketsort(buckets[1])

  return buckets[0] + buckets[1]

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
listasPiorCaso = []

tamanhos = []
duracoesAleatorio = []
duracoesPiorCaso = []

for lista in listasAleatorias:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(bucketsort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])

for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(bucketsort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Selectionsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
