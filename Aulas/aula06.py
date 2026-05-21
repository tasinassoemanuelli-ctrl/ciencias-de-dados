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
plt.Xlabel("Frutas")
plt.ylabel("Frequencia")

plt.show()
plt.savefig("aula06-qualitativo")