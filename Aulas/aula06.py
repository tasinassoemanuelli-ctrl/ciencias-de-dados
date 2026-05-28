import matplotlib.pyplot as plt
import pandas as pd 

# Análise qualitativa
frutas = [
    "Maçã", "Banana", "Maçã",
    "Laranja", "Banana", "Banana",
    "Maçã", "Uva", "Laranja"
]

serie = pd.Series(frutas)
frequencia = serie.value_counts()

print(frequencia)

# Criando gráfico de barras
frequencia.plot(kind="bar")

plt.title("Frutas Preferidas dos Alunos")
plt.xlabel("Frutas")
plt.ylabel("Frequencia")

plt.show()
plt.savefig("aula06-qualitativo")

plt.clf()

# Análise quantitativa
notas = [
    5, 6, 7, 8, 10,
    6, 5, 9, 7, 8,
    5, 6, 7, 8, 9
]

serie = pd.Series(notas)
frequencia = serie.value_counts()

print(frequencia)

serie.plot(kind="hist")

plt.title("Distribuição das notas")
plt.xlabel('Notas')
plt.ylabel("Frequência")

plt.show()
plt.savefig("aula06-quantitativo")