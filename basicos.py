import numpy as np;
import matplotlib.pyplot as plotter;

# CRIANDO MATRIZES

matB = np.array([4,5,6,7])
# print(matB)

matC = np.array(['joao', 'verde'])
# print(matC)

matD = np.array(['joao', 6, False])
# print(matD)

matE = np.zeros((3,4))
# print(matE)

def imprimeTipsMatriz(matriz):
  for item in matriz:
    print(type(item))

# print('\nimprimeTipsMatriz(matB)')
# imprimeTipsMatriz(matB)

## CRIANDO MATRIZ ALEATORIA

randomGen = np.random.default_rng(100)
matA = randomGen.random((2,3))

# print('matA', matA)

# GERAR GRAFICO

def gerarGrafico(numerosTeste, funcao, titulo):
  plotter.title(titulo)
  plotter.xlabel("x")
  plotter.ylabel("f(x)")
  plotter.plot(numerosTeste,funcao(numerosTeste))
  plotter.show()

# gerarGrafico(
#   np.linspace(00, 200, 200),
#   lambda valor: valor ** (1/2),
#   "f(x) = raiz quadrada de x"
# )

# FILTRANDO LISTAS/MATRIZES

lista = np.array([1,2,3,4,5,6,7,8,9,0])

pares = (lista % 2 == 0)
impares = (lista % 2 != 0)
maioresQue5 = (lista > 5)
# faixa = ((lista > 2) & (lista < 8))
# print(
#   lista[pares], 
#   lista[impares], 
#   lista[maioresQue5], 
#   lista[faixa],
#   sep="\n" 
# )

# CLONANDO LISTAS/MATRIZES POR VALOR

listaCopia = lista.copy()

print("lista:", lista)
print("listaCopia:", listaCopia)

listaCopia[:4] = 0

print("lista:", lista)
print("listaCopia:", listaCopia)

#  SALVAR/LER DADOS EM ARQUIVOS

dados = np.random.randint(0, 100, 10)

## Salvando
# np.save('dados-salvos', dados)
# np.savetxt('dados-salvos.csv, ', dados)

## Lendo
carregado = np.load('dados-salvos.npy')

print('carregado', carregado)

