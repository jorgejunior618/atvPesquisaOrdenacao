from time import perf_counter,sleep
from random import randint
from timeit import timeit
import math

import matplotlib.pyplot as plt
import matplotlib as mpl

# Plotando um gráfico em python na forma mais simples possível.
####
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('QUADRADOS')
plt.xlabel('VALORES')
plt.show()
####

# Plotando uma Senóide:
###
eixo_x = [ i/100.0 for i in range(628)]
eixo_y = [math.sin(i) for i in eixo_x]
plt.plot(eixo_x,eixo_y)
plt.axhline()
plt.ylabel('Seno')
plt.xlabel('Ângulo em Radianos')
plt.show()
###


# Como fazer gráficos no repl.it
###
# importar biblioteca matplotlib

# importar o pyplot

# dizer ao mpl que a figura será gerada em um arquivo
mpl.use('Agg')

# criar uma referencia para a figura com sua configuração
fig = plt.figure(figsize=(10, 8))

#ax é abreviatura de axe seria a referencia para a figura gerada dentro de um plot
# um plot pode conter n subplots (Não vamos precisar disso agora. Usando 111)
ax = fig.add_subplot(111)

#comando para plotar a figura
plt.plot([1,2,3,4],[1,4,9,16])

#definindo os rótulos do eixo y
plt.ylabel('QUADRADOS')

#definindo os rótulos do eixo x
plt.xlabel('VALORES')

# salvando o arquivo
fig.savefig('graph.png')
###

# Plotando pontos (Exemplo mostrado no tutorial)
mpl.use('Agg')
from random import randint

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

points = []
last = 0
bound = 100
for i in range(0, 100):
  last += randint(-bound, bound)
  points.append(last)

ax.plot(points)
fig.savefig('graph.png')


# Medindo o tempo de execução de uma função
###
# importa biblioteca timeit

#importa random para gerar números aleatórios

#criar uma função qualquer. No caso para gerar uma lista de números aleatórios
# vamos precisar disto
def geraLista(tam):
  lista = []
  for i in range(tam):
    n = randint(1,1*tam)
    if n not in lista: lista.append(n)
  return lista

# define o tamanho
tamanho = 1000

# roda a função 1 vez e guarda o tempo decorrido.
# se quiser rodar mais de uma vez mudar a variável number tipo number = 10
# neste caso o tempo será o tempo médio das 10 execuções.


#imprime o resultado
tempo = timeit("geraLista({})".format(tamanho),setup="from __main__ import geraLista",number=1)
print("lista gerada em {} segundos".format(tempo))


# 

# Aviso: "ATENÇÃO. Deixando aqui alguns trechos…"
# Ronaldo Fernandes Ramos
# Criado em: 11 de fev.11 de fev.
# ATENÇÃO. Deixando aqui alguns trechos de códigos que serão úteis ao longo do curso (em python).


# Uma maneira de medir o tempo em python usando perf_counter()

# Medindo o tempo método 1 - python


inicio = perf_counter()

# faz alguma coisa
sleep(2) # dormindo ...

# tempo final
fim = perf_counter()

print("Tempo duração em segundos :", fim - inicio)