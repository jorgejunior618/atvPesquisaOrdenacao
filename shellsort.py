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
  lista = np.zeros(quantidadeItens)
  novaLista = np.array(lista)
  return novaLista

############ MÉTODO DE ORDENAÇÃO ############

def shellsort(lista):
    tamanhoLista = len(lista)
    salto = 1

    while (salto < tamanhoLista):
      salto = salto * 3 + 1
    
    while (salto > 0):
      for i in range(salto, tamanhoLista):
        valorAtual = lista[i]
        j = i

        while(j >  salto - 1 and valorAtual <= lista[j - salto]):
          lista[j] = lista[j - salto]
          j -= salto
        lista[j] = valorAtual
      salto = salto // 3
    return lista

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

for lista in listasAleatorias:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(shellsort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(shellsort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração Shellsort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
