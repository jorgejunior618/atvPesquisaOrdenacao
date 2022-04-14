
class ArvoreBinaria:
  def __init__(self, dado: int):
    self.dado = dado
    self.esquerdo: ArvoreBinaria = None
    self.direito: ArvoreBinaria = None

  def criaNo(self, dado):
    '''
    Cria um novo nó e com o valor do dado informado.
    Retorna o Nó criado, mas não o adiciona à Árvore
    Para inserir um novo Nó usar [arvore].insereNo(dado)
    '''
    return ArvoreBinaria(dado)

  def pesquisar(self, dado):
    '''
    Retorna True se o valor pesquisado for encontrado na Árvore, e False caso contrário
    '''
    if (self.dado == dado):
      return True

    if (self.dado > dado):
      if (self.esquerdo != None):
        return self.esquerdo.pesquisar(dado)
      return False
    
    else:
      if (self.direito != None):
        return self.direito.pesquisar(dado)
      return False

  def imprimirArvore(self):
    '''
    Percorre toda a Árvore e imprime o valor de cada nó na ordem crescente
    '''
    if (self.esquerdo != None):
      self.esquerdo.imprimirArvore()
    print(f"{self.toString()}")
    if (self.direito != None):
      self.direito.imprimirArvore()

  def imprimirArvoreInvertida(self):
    '''
    Percorre toda a Árvore e imprime o valor de cada nó na ordem decrescente
    '''
    if (self.direito != None):
      self.direito.imprimirArvoreInvertida()
    print(f"{self}")
    if (self.esquerdo != None):
      self.esquerdo.imprimirArvoreInvertida()

  def imprimirNos(self):
    '''
    Imprime o valor de cada nó, juntamente com os nós esquero e direito.
    No formato {valor: [nó Esquerdo, nó Direito]}
    '''
    if (self == None):
      return
    
    print(
      "No: {"+
      "{:^18s}-> [{:^24s},{:^24s}]"
      .format(f"{self}", f"Esq.: {self.esquerdo}", f"Dir.: {self.direito}")
      +"}"
    )
    if (self.esquerdo != None):
      self.esquerdo.imprimirNos()
    if (self.direito != None):
      self.direito.imprimirNos()

  def menorValor(self):
    while (self.esquerdo != None):
      self = self.esquerdo

    return self.dado

  def menorValorRecursiva(self):
    if(self.esquerdo == None):
      return self.dado
    else:
      return self.menorValor(self.esquerdo)

  def maiorValor(self):
    while (self.direito != None):
      self = self.direito

    return self.dado

  def maiorValorRecursiva(self):
    if(self.direito == None):
      return self.dado
    else:
      return self.maiorValor(self.direito)

  def insereNo(self, dado):
    if (dado <= self.dado):
      if (self.esquerdo == None):
        self.esquerdo = self.criaNo(dado)
      else:
        self.esquerdo.insereNo(dado)
    else:
      if (self.direito == None):
        self.direito = self.criaNo(dado)
      else:
        self.direito.insereNo(dado)
    self._executaBalanceamento()

  def removerNo(self, dado):
    if (dado < self.dado):
      if (self.esquerdo == None):
        return False
      else:
        self.esquerdo = self.esquerdo.removerNo(dado)
    elif (dado > self.dado):
      if (self.direito == None):
        return False
      else:
        self.direito = self.direito.removerNo(dado)
    else:
      if (self.esquerdo == None and self.direito == None):
        return None
      elif (self.direito == None):
        return self.esquerdo
      elif (self.esquerdo == None):
        return self.direito
      else:
        auxiliar = self.direito.menorValor()
        self.dado = auxiliar
        self.direito = self.direito.removerNo(auxiliar)

    self._executaBalanceamento()
    return self

  def _executaBalanceamento(self):
    balanco = self._balanceamento()
    if (balanco > 1):
      if (self.esquerdo._balanceamento() > 0):
        self._rotacaoDireita()
      else:
        self._rotacaoEsquerdaDireita()
    elif (balanco < -1):
      if (self.direito._balanceamento() < 0):
        self._rotacaoEsquerda()
      else:
        self._rotacaoDireitaEsquerda()

  def _balanceamento(self) -> int:
      profundidadeEsq = 0
      profundidadeDir = 0

      if (self.esquerdo != None):
          profundidadeEsq = self.esquerdo._profundidade()
      if (self.direito != None):
          profundidadeDir = self.direito._profundidade()

      return profundidadeEsq - profundidadeDir

  def _profundidade(self) -> int:
      profundidadeEsq = 0
      profundidadeDir = 0

      if (self.esquerdo != None):
          profundidadeEsq = self.esquerdo._profundidade()
      if (self.direito != None):
          profundidadeDir = self.direito._profundidade()

      return 1 + max(profundidadeEsq, profundidadeDir)
  
  def definirFilhos(self, esquerdo, direito):
    self.esquerdo = esquerdo
    self.direito = direito

  def _rotacaoEsquerda(self):
    self.dado, self.direito.dado = self.direito.dado, self.dado
    esquerdoInicial = self.esquerdo
    self.definirFilhos(self.direito, self.direito.direito)
    self.esquerdo.definirFilhos(esquerdoInicial, self.esquerdo.esquerdo)

  def _rotacaoDireita(self):
    self.dado, self.esquerdo.dado = self.esquerdo.dado, self.dado
    direitoInicial = self.direito
    self.definirFilhos(self.esquerdo.esquerdo, self.esquerdo)
    self.direito.definirFilhos(self.direito.direito, direitoInicial)

  def _rotacaoEsquerdaDireita(self):
    self.esquerdo._rotacaoEsquerda()
    self._rotacaoDireita()

  def _rotacaoDireitaEsquerda(self):
    self.direito._rotacaoDireita()
    self._rotacaoEsquerda()

  def toString(self):
    return (
      "{ "
      + "{:2d}".format(self.dado)
      + " }"
    )
	
  def __str__(self):
    return (
      "{ "
      + "{:2d}, Bal: {:3d}".format(self.dado ,self._balanceamento())
      + " }"
    )

arvere = ArvoreBinaria(5)
arvere.insereNo(15)
arvere.insereNo(3)
arvere.insereNo(18)
arvere.insereNo(1)
arvere.insereNo(4)
arvere.insereNo(13)
arvere.insereNo(20)

arvere.imprimirNos()
print("\n\n\nVai apagar")
arvere = arvere.removerNo(1)
print("Apagou 1")
arvere.imprimirNos()
arvere.imprimirArvore()
