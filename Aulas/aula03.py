import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [200, 300, 340, 305, 360, 360]

plt.plot(meses, vendas, color='pink')
plt.title('Vendas no Primeiro Semestre')

plt.xlabel('Meses')
plt.ylabel('Vendas')

plt.show()
plt.savefig('aula03')