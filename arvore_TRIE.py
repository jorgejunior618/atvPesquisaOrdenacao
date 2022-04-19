class NoTrie:
  def __init__(self, chave: str or None, dado: int or None):
    self.chave = chave
    self.dado = dado
    self.filhos: list[NoTrie] = []

  def imprimeNos(self):
    print(self.toString())
    print("  filhos: [", end=" ")
    for noFilho in self.filhos:
      print(noFilho.chave, end=",")
    print(" ]")
    if(len(self.filhos) > 0):
      for noFilho in self.filhos:
        noFilho.imprimeNos()

  def toString(self):
    return "No: { " + f"'{self.chave}', {self.dado}" + " }"

class ArvoreTrie:
  def __init__(self):
    self.raiz: NoTrie = NoTrie(None, None)
    self._ultimoValor = 0

  def inserePalavra(self, palavra: str):
    tamanhoPalavra = len(palavra)
    ultimoNo  = self.raiz

    for i in range(tamanhoPalavra):
      ultimoNo =  self._insereNo(
        ultimoNo,
        palavra[i],
        i == tamanhoPalavra -1
      )

  def _insereNo(self, no: NoTrie, chave: str, ultima: bool) -> NoTrie:

    for filho in no.filhos:
      if (filho.chave == chave):
        if (ultima and filho.dado == None):
          filho.dado = self._ultimoValor
          self._ultimoValor += 1
        return filho

    valorAinserir = None

    if (ultima):
      valorAinserir = self._ultimoValor
      self._ultimoValor += 1

    ultimoNo = NoTrie(chave, valorAinserir)
    no.filhos.append(ultimoNo)

    return ultimoNo

  def buscaPalavra(self, palavra: str) -> int:
    tamanhoPalavra = len(palavra)
    ultimoNo  = self.raiz

    for i in range(tamanhoPalavra):
      ultimoNo =  self._buscaNo(
        ultimoNo,
        palavra[i],
        i == tamanhoPalavra -1
      )
      if (ultimoNo == None):
        return None
    return ultimoNo.dado

  def _buscaNo(self, no: NoTrie, chave: str, ultima: bool) -> NoTrie:
    ultimoNo = None

    for filho in no.filhos:
      if (filho.chave == chave):
        if (ultima):
          if (filho.chave != chave or filho.dado == None):
            return None
          return filho
        return filho

    return ultimoNo

  def removePalavra(self, palavra: str) -> int:
    valorPalavra = self.buscaPalavra(palavra)
    if (valorPalavra == None): return

    tamanhoPalavra = len(palavra)
    ultimoNo  = self.raiz
    removiveis: list[bool] = []

    for i in range(tamanhoPalavra):
      ultimoNo =  self._buscaNo(
        ultimoNo,
        palavra[i],
        i == tamanhoPalavra -1
      )

      removivel = (len(ultimoNo.filhos) <= 1
        and (ultimoNo.dado == None or ultimoNo.dado == valorPalavra))

      if (i == tamanhoPalavra -1):
        removivel = removivel and len(ultimoNo.filhos) == 0
      removiveis.append(removivel)
    
    ultimoRemovivel = 0

    for i in range(tamanhoPalavra):
      if (not removiveis[i]):
        ultimoRemovivel = i+1

    if (ultimoRemovivel == tamanhoPalavra and len(ultimoNo.filhos) > 0):
      ultimoNo.dado = None
      return

    ultimoNo  = self.raiz
    for i in range(ultimoRemovivel):
      ultimoNo =  self._buscaNo(
        ultimoNo,
        palavra[i],
        i == tamanhoPalavra -1
      )

    for i in range(len(ultimoNo.filhos)):
      if(ultimoNo.filhos[i].chave == palavra[ultimoRemovivel]):
        ultimoNo.filhos.pop(i)
        break

  def _removeNo(self, no: NoTrie, chave: str, ultima: bool) -> NoTrie:
    ultimoNo = None

    return ultimoNo

  def imprimeArvore(self):
    self.raiz.imprimeNos()

arvere = ArvoreTrie()

arvere.inserePalavra("by")
arvere.inserePalavra("sea")
arvere.inserePalavra("sells")
arvere.inserePalavra("shels")
arvere.inserePalavra("the")
arvere.inserePalavra("she")
print("\nImprimindo Arvore")
print("=======================================")
arvere.imprimeArvore()
print("\nBuscando palavra 'the'")
print(f'achou "the": {arvere.buscaPalavra("the")}')
print("\nBuscando palavra 'by'")
print(f'achou "by": {arvere.buscaPalavra("by")}')
print("\nBuscando palavra 'sea'")
print(f'achou "sea": {arvere.buscaPalavra("sea")}')
print("\nBuscando palavra 'she'")
print(f'achou "she": {arvere.buscaPalavra("she")}')
print("\nBuscando palavra 'sells'")
print(f'achou "sells": {arvere.buscaPalavra("sells")}')
print("\nBuscando palavra 'shels'")
print(f'achou "shels": {arvere.buscaPalavra("shels")}')

print("\nRemovendo a palavra 'shels'")
arvere.removePalavra("shels")
print("\nImprimindo Arvore")
print("=======================================")
arvere.imprimeArvore()

print("\nBuscando palavra 'she'")
print(f'achou "she": {arvere.buscaPalavra("she")}')
print("\nBuscando palavra 'shels'")
print(f'achou "shels": {arvere.buscaPalavra("shels")}')
