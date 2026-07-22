#Por fim, conseguimos visualizar a quantidade de homens e mulheres com doença cardíaca, dispostos no mesmo gráfico para melhor visualização.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df_2 = pd.read_csv("df_2.csv")

plt.figure(figsize=(8,5))

idade_homens = df_doenca[df_doenca["Sexo"] == "M"]["Idade"]
idade_mulheres = df_doenca[df_doenca["Sexo"] == "F"]["Idade"]

plt.hist(idade_homens, bins=15, alpha=0.6, label="Homens",edgecolor="gray" )
plt.hist(idade_mulheres, bins=15, alpha=0.7, label="Mulheres",edgecolor="gray")

plt.title("Distribuição das idades dos pacientes com doença cardíaca por sexo")
plt.xlabel("Idade (anos)")
plt.ylabel("Número de pacientes")
plt.legend()

plt.show()
