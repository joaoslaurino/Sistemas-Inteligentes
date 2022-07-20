from matplotlib import pyplot as plt
from genetic2022 import *
from bruteforce import *
import time

#Definindo itens possíveis (número de pessoas tagueadas, likes)
maxtag = 3
itens = [(1 ,5),(3 ,76) ,(7, 248) ,(2, 25) ,(5, 169) ,(2, 37) ,(6, 352) ,(1, 8) ,(2, 49) ,(1, 133),(9, 561),(2,15),
(13,1562),(1,4),(2,12),(1 ,5),(3 ,76) ,(1, 248) ,(2, 25) ,(5, 169) ,(2, 37) ,(3, 352) ,(1, 8) ,(3, 49) ,(2, 133)]

#Removendo as fotos que tem um número de pessoas tagueadas maior que 3
i = 0
n_itens = len(itens)
while(i<n_itens):
  if (itens[i][0] > 3):
    itens.remove(itens[i])
    i-=1
    n_itens-=1
  i += 1  

#Número de itens
n_itens = len(itens)
print("Nro de itens: "+str(n_itens)) 
likes_max = 50 #Quantidade de likes máxima

#Calcula valor de validação com brute force
t0 = time.time()
best = run_bruteforce(itens, likes_max)
t1 = time.time()
print("Tempo Brute force: "+str(t1-t0))
t0 = time.time()

#Tamanho da população
p_count = 100

#Criando a população
p = population(p_count , n_itens)

#Número de gerações para testar
epochs = 1000

#Salva fitness para referência
media = media_fitness(p, itens, likes_max)
best_f = best_fitness(p, itens, likes_max)
fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]] # med fitness|med likes|best fitness|best likes

for i in range(epochs):
    p = evolve(p, itens , likes_max)
    media = media_fitness(p, itens, likes_max)
    best_f = best_fitness(p, itens, likes_max)
    fitness_history[0].append(media[0])
    fitness_history[1].append(media[1])
    fitness_history[2].append(best_f[0])
    fitness_history[3].append(best_f[1])

t1 = time.time()

#funções para printar os valores no console

print("Individuo Brute Force (Combinação de fotos): "+str(best[1])+", Likes: "+str(best[0]))

print("Tempo AG: "+str(t1-t0))

print("Individuo AG (Combinação de fotos): "+str(sorted(p, key=lambda p:p[0])[-1])+", Likes: " +str(fitness_history[2][-1]))

#funções para plotar o grafico

fig = plt.figure()
ax = plt.axes()

ax.plot(fitness_history[0])
ax.plot(fitness_history[2])
ax.plot([best[0] for i in fitness_history[0]])
ax.plot(fitness_history[1])
ax.plot(fitness_history[3])

ax.legend(["Fitness Media", "Melhor Fitness", "Fitness Brute Force", "Media de likes (x10)", "Likes das melhores fotos (x10)"])

ax.grid(True)
plt.show()
