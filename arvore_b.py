class NoB:
  def __init__(self, ehFolha=False):
    self.ehFolha = ehFolha or False
    self.chaves = []
    self.filhos = []


# Tree
class ArvoreB:
  def __init__(self, ordem):
    self.raiz = NoB(True)
    self.ordem = ordem

    # Insert node
  def insereNo(self, dado):
    raiz = self.raiz

    if (len(raiz.chaves) == (2 * self.ordem) - 1):
      noAuxiliar = NoB()
      self.raiz = noAuxiliar

      noAuxiliar.filhos.insert(0, raiz)
      self.dividirFilhos(noAuxiliar, 0)
      self._inserirNoListaNaoCheia(noAuxiliar, dado)
    else:
      self._inserirNoListaNaoCheia(raiz, dado)

    # Insert nonfull
  def _inserirNoListaNaoCheia(self, raiz: NoB, dado):
    tamanhoListaFilhos = len(raiz.chaves) - 1

    if (raiz.ehFolha):
      raiz.chaves.append(None)

      while (tamanhoListaFilhos >= 0 and dado < raiz.chaves[tamanhoListaFilhos]):
        raiz.chaves[tamanhoListaFilhos + 1] = raiz.chaves[tamanhoListaFilhos]
        tamanhoListaFilhos -= 1
      raiz.chaves[tamanhoListaFilhos + 1] = dado
    else:
      while (tamanhoListaFilhos >= 0 and dado < raiz.chaves[tamanhoListaFilhos]):
        tamanhoListaFilhos -= 1
      tamanhoListaFilhos += 1

      if (len(raiz.filhos[tamanhoListaFilhos].chaves) == (2 * self.ordem) - 1):
        self.dividirFilhos(raiz, tamanhoListaFilhos)
        if (dado > raiz.chaves[tamanhoListaFilhos]):
          tamanhoListaFilhos += 1
      self._inserirNoListaNaoCheia(raiz.filhos[tamanhoListaFilhos], dado)

    # Split the filhos
  def dividirFilhos(self, raiz: NoB, tamanhoListaFilhos):
    ordemAtual = self.ordem
    nohAtual = raiz.filhos[tamanhoListaFilhos]
    novoNoh = NoB(nohAtual.ehFolha)

    raiz.filhos.insert(tamanhoListaFilhos + 1, novoNoh)
    raiz.chaves.insert(tamanhoListaFilhos, nohAtual.chaves[ordemAtual - 1])
    novoNoh.chaves = nohAtual.chaves[ordemAtual: (2 * ordemAtual) - 1]
    nohAtual.chaves = nohAtual.chaves[0: ordemAtual - 1]

    if (not nohAtual.ehFolha):
      novoNoh.filhos = nohAtual.filhos[ordemAtual: 2 * ordemAtual]
      nohAtual.filhos = nohAtual.filhos[0: ordemAtual - 1]

  # Print the tree
  def imprimirArvore(self, raiz: NoB, nivel=0):
    print("Nível ", nivel, end=":")

    # for i in raiz.chaves:
    #   print(i, end=" ")
    print(raiz.chaves)

    nivel += 1
    if (len(raiz.filhos) > 0):
      for i in raiz.filhos:
        self.imprimirArvore(i, nivel)

  # Search key in the tree
  def buscarChave(self, k, x=None):
    if (x is not None):
      i = 0
      while (i < len(x.chaves) and k > x.chaves[i]):
        i += 1
      if (i < len(x.chaves) and k == x.chaves[i]):
        return (x, i)
      elif (x.ehFolha):
        return None
      else:
        return self.buscarChave(k, x.filhos[i])
      
    else:
      return self.buscarChave(k, self.raiz)


# B = ArvoreB(3)

# for i in range(10):
#   B.insereNo(2 * i)

# print("\n ####### Imprimindo Árvore ordenada #######")
# print(" ==========================================")
# B.imprimirArvore(B.raiz)


print("\n ####### Inserindo os Valores: 5, 15, 3, 18, 1, 4, 13, 20 #######")
arvere = ArvoreB(2)
arvere.insereNo(15)
arvere.insereNo(3)
arvere.insereNo(18)
arvere.insereNo(8)
arvere.insereNo(1)
arvere.insereNo(4)
arvere.insereNo(13)
arvere.insereNo(20)

print("\n ####### Imprimindo Árvore ordenada #######")
print(" ==========================================")
arvere.imprimirArvore(arvere.raiz)
# print("\n ####### Imprimindo cada Nó da Árvore com seus respectivos filhos #######")
# print(" ========================================================================")
# arvere.imprimirNos()

# print("\n ####### Removendo a Raíz #######")
# arvere = arvere.removerNo(5)

print("\n ####### Imprimindo Árvore ordenada #######")
print(" ==========================================")
arvere.imprimirArvore(arvere.raiz)
# print("\n ####### Imprimindo cada Nó da Árvore com seus respectivos filhos #######")
# print(" ========================================================================")
# arvere.imprimirNos()
