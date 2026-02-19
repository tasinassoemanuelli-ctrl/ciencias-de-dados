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

