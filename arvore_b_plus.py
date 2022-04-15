import math

class NoBplus:
    def __init__(self, ordem):
        self.ordem = ordem
        self.valores = []
        self.chaves = []
        self.proximaChave = None
        self.noPai = None
        self.checarFolha = False

    def inserirNaFolha(self, value, key):
        if (self.valores):
            temp1 = self.valores
            for i in range(len(temp1)):
                if (value == temp1[i]):
                    self.chaves[i].append(key)
                    break
                elif (value < temp1[i]):
                    self.valores = self.valores[:i] + [value] + self.valores[i:]
                    self.chaves = self.chaves[:i] + [[key]] + self.chaves[i:]
                    break
                elif (i + 1 == len(temp1)):
                    self.valores.append(value)
                    self.chaves.append([key])
                    break
        else:
            self.valores = [value]
            self.chaves = [[key]]


class ArvoreBplus:
    def __init__(self, ordem):
        self.raiz = NoBplus(ordem)
        self.raiz.checarFolha = True

    def insereNo(self, valor, chave):
        old_node = self.buscar(valor)
        old_node.inserirNaFolha(valor, chave)

        if (len(old_node.valores) == old_node.ordem):
            node1 = NoBplus(old_node.ordem)
            node1.checarFolha = True
            node1.noPai = old_node.noPai
            mid = int(math.ceil(old_node.ordem / 2)) - 1
            node1.valores = old_node.valores[mid + 1:]
            node1.chaves = old_node.chaves[mid + 1:]
            node1.proximaChave = old_node.proximaChave
            old_node.valores = old_node.valores[:mid + 1]
            old_node.chaves = old_node.chaves[:mid + 1]
            old_node.proximaChave = node1
            self.inserirNoPai(old_node, node1.valores[0], node1)

    def buscar(self, valor):
        current_node = self.raiz
        while(current_node.checarFolha == False):
            temp2 = current_node.valores
            for i in range(len(temp2)):
                if (valor == temp2[i]):
                    current_node = current_node.chaves[i + 1]
                    break
                elif (valor < temp2[i]):
                    current_node = current_node.chaves[i]
                    break
                elif (i + 1 == len(current_node.valores)):
                    current_node = current_node.chaves[i + 1]
                    break
        return current_node

    def find(self, valor, chave):
        l = self.buscar(valor)
        for i, item in enumerate(l.valores):
            if item == valor:
                if chave in l.chaves[i]:
                    return True
                else:
                    return False
        return False

    def inserirNoPai(self, no, valor, ndash):
        if (self.raiz == no):
            rootNode = NoBplus(no.ordem)
            rootNode.valores = [valor]
            rootNode.chaves = [no, ndash]
            self.raiz = rootNode
            no.parent = rootNode
            ndash.parent = rootNode
            return

        parentNode = no.parent
        temp3 = parentNode.chaves
        for i in range(len(temp3)):
            if (temp3[i] == no):
                parentNode.valores = parentNode.valores[:i] + \
                    [valor] + parentNode.valores[i:]
                parentNode.chaves = parentNode.chaves[:i +
                                                  1] + [ndash] + parentNode.chaves[i + 1:]
                if (len(parentNode.chaves) > parentNode.ordem):
                    parentdash = NoBplus(parentNode.ordem)
                    parentdash.noPai = parentNode.parent
                    mid = int(math.ceil(parentNode.ordem / 2)) - 1
                    parentdash.valores = parentNode.valores[mid + 1:]
                    parentdash.chaves = parentNode.chaves[mid + 1:]
                    valor_ = parentNode.valores[mid]
                    if (mid == 0):
                        parentNode.valores = parentNode.valores[:mid + 1]
                    else:
                        parentNode.valores = parentNode.valores[:mid]
                    parentNode.chaves = parentNode.chaves[:mid + 1]
                    for j in parentNode.chaves:
                        j.parent = parentNode
                    for j in parentdash.chaves:
                        j.parent = parentdash
                    self.inserirNoPai(parentNode, valor_, parentdash)

    def removerNo(self, valor, chave):
        node_ = self.buscar(valor)

        temp = 0
        for i, item in enumerate(node_.valores):
            if item == valor:
                temp = 1

                if chave in node_.chaves[i]:
                    if len(node_.chaves[i]) > 1:
                        node_.chaves[i].pop(node_.chaves[i].index(chave))
                    elif node_ == self.raiz:
                        node_.valores.pop(i)
                        node_.chaves.pop(i)
                    else:
                        node_.chaves[i].pop(node_.chaves[i].index(chave))
                        del node_.chaves[i]
                        node_.valores.pop(node_.valores.index(valor))
                        self.deletarEntrada(node_, valor, chave)
                else:
                    print("Valor não está na chave")
                    return
        if temp == 0:
            print("Valor não encontrado")
            return

    def deletarEntrada(self, no, valor, chave):

        if not no.checarFolha:
            for i, item in enumerate(no.chaves):
                if item == chave:
                    no.chaves.pop(i)
                    break
            for i, item in enumerate(no.valores):
                if item == valor:
                    no.valores.pop(i)
                    break

        if self.raiz == no and len(no.chaves) == 1:
            self.raiz = no.chaves[0]
            no.chaves[0].parent = None
            del no
            return
        elif (len(no.chaves) < int(math.ceil(no.ordem / 2)) and no.checarFolha == False) or (len(no.valores) < int(math.ceil((no.ordem - 1) / 2)) and no.checarFolha == True):

            is_predecessor = 0
            parentNode = no.parent
            PrevNode = -1
            NextNode = -1
            PrevK = -1
            PostK = -1
            for i, item in enumerate(parentNode.chaves):

                if item == no:
                    if i > 0:
                        PrevNode = parentNode.chaves[i - 1]
                        PrevK = parentNode.valores[i - 1]

                    if i < len(parentNode.chaves) - 1:
                        NextNode = parentNode.chaves[i + 1]
                        PostK = parentNode.valores[i]

            if PrevNode == -1:
                ndash = NextNode
                valor_ = PostK
            elif NextNode == -1:
                is_predecessor = 1
                ndash = PrevNode
                valor_ = PrevK
            else:
                if len(no.valores) + len(NextNode.valores) < no.ordem:
                    ndash = NextNode
                    valor_ = PostK
                else:
                    is_predecessor = 1
                    ndash = PrevNode
                    valor_ = PrevK

            if len(no.valores) + len(ndash.valores) < no.ordem:
                if is_predecessor == 0:
                    no, ndash = ndash, no
                ndash.chaves += no.chaves
                if not no.checarFolha:
                    ndash.valores.append(valor_)
                else:
                    ndash.proximaChave = no.proximaChave
                ndash.valores += no.valores

                if not ndash.checarFolha:
                    for j in ndash.chaves:
                        j.parent = ndash

                self.deletarEntrada(no.parent, valor_, no)
                del no
            else:
                if is_predecessor == 1:
                    if not no.checarFolha:
                        ndashpm = ndash.chaves.pop(-1)
                        ndashkm_1 = ndash.valores.pop(-1)
                        no.chaves = [ndashpm] + no.chaves
                        no.valores = [valor_] + no.valores
                        parentNode = no.parent
                        for i, item in enumerate(parentNode.valores):
                            if item == valor_:
                                parentNode.valores[i] = ndashkm_1
                                break
                    else:
                        ndashpm = ndash.chaves.pop(-1)
                        ndashkm = ndash.valores.pop(-1)
                        no.chaves = [ndashpm] + no.chaves
                        no.valores = [ndashkm] + no.valores
                        parentNode = no.parent
                        for i, item in enumerate(parentNode.valores):
                            if item == valor_:
                                parentNode.valores[i] = ndashkm
                                break
                else:
                    if not no.checarFolha:
                        ndashp0 = ndash.chaves.pop(0)
                        ndashk0 = ndash.valores.pop(0)
                        no.chaves = no.chaves + [ndashp0]
                        no.valores = no.valores + [valor_]
                        parentNode = no.parent
                        for i, item in enumerate(parentNode.valores):
                            if item == valor_:
                                parentNode.valores[i] = ndashk0
                                break
                    else:
                        ndashp0 = ndash.chaves.pop(0)
                        ndashk0 = ndash.valores.pop(0)
                        no.chaves = no.chaves + [ndashp0]
                        no.valores = no.valores + [ndashk0]
                        parentNode = no.parent
                        for i, item in enumerate(parentNode.valores):
                            if item == valor_:
                                parentNode.valores[i] = ndash.valores[0]
                                break

                if not ndash.checarFolha:
                    for j in ndash.chaves:
                        j.parent = ndash
                if not no.checarFolha:
                    for j in no.chaves:
                        j.parent = no
                if not parentNode.checarFolha:
                    for j in parentNode.chaves:
                        j.parent = parentNode

def imprimirArvore(tree):
    lst = [tree.raiz]
    level = [0]
    leaf = None
    flag = 0
    lev_leaf = 0

    node1 = NoBplus(str(level[0]) + str(tree.raiz.valores))

    while (len(lst) != 0):
        x = lst.pop(0)
        lev = level.pop(0)
        if (x.checarFolha == False):
            for i, item in enumerate(x.chaves):
                print(item.valores)
        else:
            for i, item in enumerate(x.chaves):
                print(item.valores)
            if (flag == 0):
                lev_leaf = lev
                leaf = x
                flag = 1


arvere = ArvoreBplus(3)
arvere.insereNo(5, 33)
arvere.insereNo(15, 21)
arvere.insereNo(25, 31)
arvere.insereNo(35, 41)
arvere.insereNo(45, 10)

print("\n ####### Imprimindo Árvore ordenada #######")
print(" ==========================================")
imprimirArvore(arvere)

print("\n ####### Removendo a chave (5, 33) #######")
arvere.removerNo(5, 33)

print("\n ####### Imprimindo Árvore ordenada #######")
print(" ==========================================")
imprimirArvore(arvere)
