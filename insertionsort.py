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

def insertionsort(lista):
  tamanhoLista = len(lista)

  for atual in range(1, tamanhoLista):
    indiceMenor = atual

    for i in range(atual - 1, -1, -1):
      if(lista[atual] < lista[i]):
        indiceMenor = i
      else: break

    if(indiceMenor != atual):
      valorAtual = lista[atual]
      lista = np.delete(lista, atual)
      lista = np.insert(lista, indiceMenor, valorAtual)

  return lista

############ VARIÁVEIS E PROGRAMA ############

listasAleatorias = [
  geraLista(1000),
  geraLista(2000),
  geraLista(3000),
  geraLista(4000),
  geraLista(5000),
  geraLista(8000),
  geraLista(11000),
  geraLista(15000)
]

listasOrdenadas = []
listasPiorCaso = []

tamanhos = []
duracoesAleatorio = []
duracoesPiorCaso = []

for lista in listasAleatorias:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(insertionsort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])

for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(insertionsort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Selectionsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
