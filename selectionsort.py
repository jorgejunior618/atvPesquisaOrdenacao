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

def selectionsort(lista):
  tamanhoLista = len(lista)

  for primeiro in range(tamanhoLista):
    indiceMenor = primeiro

    for i in range(indiceMenor + 1, tamanhoLista):
      if(lista[indiceMenor] > lista[i]):
        indiceMenor = i

    lista[primeiro], lista[indiceMenor] = lista[indiceMenor], lista[primeiro]

  return lista

############ VARIÁVEIS E PROGRAMA ############

listasAleatorias = [
  geraLista(1),
  geraLista(2),
  geraLista(3),
  geraLista(4),
  geraLista(5),
  geraLista(8),
  # geraLista(1000),
  # geraLista(2000),
  # geraLista(3000),
  # geraLista(4000),
  # geraLista(5000),
  # geraLista(8000),
  # geraLista(11000),
  # geraLista(15000)
]

listasOrdenadas = []
listasPiorCaso = []

tamanhos = []
duracoesAleatorio = []
duracoesPiorCaso = []

print('listasAleatorias')
for lista in listasAleatorias:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(selectionsort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])

print('\n\n\nlistasPiorCaso')
for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(selectionsort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Selectionsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
