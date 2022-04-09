from time import perf_counter
import numpy as np;
import matplotlib.pyplot as plotter;

class ArvoreHeap:
  def __init__(self, tamanhoTotal: int):
    self.raiz = None
    self.matrizHeap = []
    self.tamanhoAtual = 0
    self.tamanhoTotal = tamanhoTotal

    for i in range(tamanhoTotal):
      self.matrizHeap.append(None)

  def insereNo(self, dado):
    '''
    Adiciona um novo nó à Árvore com o valor do dado informado e orageniza sua posição mantendo o padrão Heap
    '''
    novoNo = dado
    self.matrizHeap[self.tamanhoAtual] = novoNo
    self.organizaPosicaoAcima(self.tamanhoAtual)
    self.tamanhoAtual += 1

  def removeMaiorNo(self):
    '''
    Remove o elemento de maior valor da Array que representa a árvore e a reorganiza.
    Retorno: valor do elemento removido
    '''
    maiorNo = self.matrizHeap[0]
    self.tamanhoAtual -= 1
    self.matrizHeap[0] = self.matrizHeap[self.tamanhoAtual]
    self.organizaPosicaoAbaixo(0)

    return maiorNo

  def organizaPosicaoAcima(self, indice): # ->    indice = 3
    '''
    Move à cima o valor do indice informado, colocando o em sua devida posição na Array que representa a Árvore
    '''
    indiceUtil = indice
    indicePai = (indiceUtil - 1) // 2
    base = self.matrizHeap[indiceUtil]

    while (indiceUtil > 0 and self.matrizHeap[indicePai] < base):
      self.matrizHeap[indiceUtil] = self.matrizHeap[indicePai]
      indiceUtil = indicePai
      indicePai = (indicePai - 1) // 2
    
    self.matrizHeap[indiceUtil] = base

  def organizaPosicaoAbaixo(self, indice):
    '''
    Move à baixo o valor do indice informado, colocando o em sua devida posição na Array que representa a Árvore
    '''
    indiceUtil = indice
    topo = self.matrizHeap[indiceUtil]

    while (indiceUtil < self.tamanhoAtual / 2):
      filhoEsquerdo = self.noEsquerdo(indiceUtil)
      filhoDireito = self.noDireito(indiceUtil)

      if (filhoDireito < self.tamanhoAtual and self.matrizHeap[filhoEsquerdo] < self.matrizHeap[filhoDireito]):
        filhoMaior = filhoDireito
      else:
        filhoMaior = filhoEsquerdo
      if (topo >= self.matrizHeap[filhoMaior]): break
      self.matrizHeap[indiceUtil] = self.matrizHeap[filhoMaior]
      indiceUtil = filhoMaior
    
    self.matrizHeap[indiceUtil] = topo

  def noPai(self, indice):
    return (indice - 1) // 2

  def noEsquerdo(self, indice,):
    indiceNo = indice * 2 + 1
    return indiceNo

  def noDireito(self, indice,):
    indiceNo = indice * 2 + 2
    return indiceNo

  def limpaArvore(self):
    '''
    Remove todos os itens armazenados na arvore, varrendo-a com o removeMaiorNo.
    Armzena os itens em uma array ordenda.
    Retorno: todos os itens da Árvore em ordem crescecnte
    '''
    listaInvertida = []
    for i in range(self.tamanhoTotal):
      listaInvertida.append(self.removeMaiorNo())
    
    return listaInvertida[::-1]
############ Fim da Classe Arvore Heap ############


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
def heapSort(lista):
  tamanhoLista = len(lista)
  arvore = ArvoreHeap(tamanhoLista)

  for indice in range(tamanhoLista):
    arvore.insereNo(lista[indice])

  return arvore.limpaArvore()

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
    lambda : listasOrdenadas.append(heapSort(lista.copy()))
  )
  tamanhos.append(len(lista))
  duracoesAleatorio.append(arredondar(duracaoOrdenacao, 4))

for lista in listasOrdenadas:
  listasPiorCaso.append(lista[::-1])

for lista in listasPiorCaso:
  duracaoOrdenacao = medirTempo(
    lambda : listasOrdenadas.append(heapSort(lista.copy()))
  )
  duracoesPiorCaso.append(arredondar(duracaoOrdenacao, 4))

plotter.title("Duração HeapSort")
plotter.xlabel("Tamanho das Séries")
plotter.ylabel("Tempo")
plotter.plot(tamanhos, duracoesAleatorio, label="Aleatória")
plotter.plot(tamanhos, duracoesPiorCaso, label="Pior caso")
plotter.legend()
plotter.show()
