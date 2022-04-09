class No:
  dado, esquerdo, direito = 0, None, None

  def __init__(self, dado):
    self.esquerdo = None
    self.direito = None
    self.dado = dado

  def __str__(self):
    return "{",str(self.dado),"}"

class ArvoreBinaria:
  def __init__(self):
    self.raiz = None

  def criaNo(self, dado):
    '''
    Cria um novo nó e com o valor do dado informado.
    Retorna o Nó criado, mas não o adiciona à Árvore
    Para inserir um novo Nó usar [arvore].insereNo(dado)
    '''
    return No(dado)

  def insereNo(self, raiz: No, dado):
    '''
    Adiciona um novo nó à Árvore com o valor do dado informado
    '''
    if (raiz == None):
      return self.criaNo(dado)
    if (raiz.dado >= dado):
      raiz.esquerdo = self.insereNo(raiz.esquerdo, dado)
    else:
      raiz.direito = self.insereNo(raiz.direito, dado)
    
    return raiz

  def pesquisar(self, raiz: No, dado):
    '''
    Retorna True se o valor pesquisado for encontrado na Árvore, e False caso contrário
    '''
    if (raiz == None):
      return False
    
    if (raiz.dado == dado):
      return True

    if (raiz.dado > dado):
      return self.pesquisar(raiz.esquerdo, dado)
    
    else:
      return self.pesquisar(raiz.direito, dado)

  def imprimirArvore(self, raiz: No):
    '''
    Percorre toda a Árvore e imprime o valor de cada nó na ordem crescente
    '''
    if (raiz == None):
      return
    
    self.imprimirArvore(raiz.esquerdo)
    print(f"{raiz}")
    self.imprimirArvore(raiz.direito)

  def imprimirArvoreInvertida(self, raiz: No):
    '''
    Percorre toda a Árvore e imprime o valor de cada nó na ordem decrescente
    '''
    if (raiz == None):
      return
    
    self.imprimirArvoreInvertida(raiz.direito)
    print(f"{raiz}")
    self.imprimirArvoreInvertida(raiz.esquerdo)

  def imprimirNos(self, raiz: No):
    '''
    Imprime o valor de cada nó, juntamente com os nós esquero e direito.
    No formato {valor: [nó Esquerdo, nó Direito]}
    '''
    if (raiz == None):
      return
    
    dadoRaiz = raiz.dado
    dadoEsquerdo = None
    dadoDireito = None

    if (raiz.esquerdo != None):
      dadoEsquerdo = raiz.esquerdo.dado
    if (raiz.direito != None):
      dadoDireito = raiz.direito.dado

    print("{"+f"{dadoRaiz}: [{dadoEsquerdo}, {dadoDireito}]"+"}")
    self.imprimirNos(raiz.esquerdo)
    self.imprimirNos(raiz.direito)

  def menorValor(self, raiz: No):
    while (raiz.esquerdo != None):
      raiz = raiz.esquerdo

    return raiz.dado

  def menorValorRecursiva(self, raiz: No):
    if(raiz.esquerdo == None):
      return raiz.dado
    else:
      return self.menorValor(raiz.esquerdo)

  def maiorValor(self, raiz: No):
    while (raiz.direito != None):
      raiz = raiz.direito

    return raiz.dado

  def maiorValorRecursiva(self, raiz: No):
    if(raiz.direito == None):
      return raiz.dado
    else:
      return self.maiorValor(raiz.direito)

  def _fimArvoreBinara():
    pass

arvere = ArvoreBinaria()
