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
  return np.random.randint(0, quantidadeItens, quantidadeItens)

############ MÉTODO DE ORDENAÇÃO ############
def bubblesort(lista):
  inversoes = 1
  tamanhoLista = len(lista)

  while (inversoes != 0):
    inversoes = 0
    for i in range(tamanhoLista):
      if (i + 1 == tamanhoLista): 
        break

      if (lista[i] > lista[i + 1]):
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
        inversoes += 1

  return lista


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

for i in range(len(listasAleatorias)):
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(bubblesort(listasAleatorias[i]))
  )
  tamanhos.append(len(listasAleatorias[i]))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])
  
for i in range(len(listasPiorCaso)):
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(bubblesort(listasPiorCaso[i]))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Bubblesort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
