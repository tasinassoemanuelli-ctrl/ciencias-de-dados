# Exercicio 01 - 1) Construa um gráfico de barras que compare a nota de popularidade de séries em 2025:

import matplotlib.pyplot as plt

categorias = ['Stranger Things', 'It', 'Game of Thrones', 'Friends']
valores = [5.0, 3.5, 2.3, 1.1]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex01.png')


# Exercicio 02 - 2) Construa um gráfico de barras que compare os celulares mais vendidos em 2026:

# Ele limpa o gráfico criado, para criar novos
plt.clf()

categorias = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valores = [200000, 320000, 500000]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex02.png')

#Exercicio 03 - 3) Identifique na turma qual é o time de cada um e construa um gráfico de barras para mostrar a popularidade cada time.
# Grêmio: 3, Flamengo: 2, Palmeiras: 1, Internacional: 2, Vasco: 1
plt.clf()

times = ['Gremio', 'Flamengo', 'Palmeiras', 'internacional', 'Vasco']
torcedores = [3, 2, 1, 2, 1]
cores = ['#0D80BF', '#C52613', '#006437', '#E5050F', '#000000']

plt.bar(times, torcedores, color=cores)
plt.xlabel('Times do campeonato brasileiro')
plt.ylabel('N° de torcedores')
plt.show()
plt.savefig('./exercicios/ex03.png')
