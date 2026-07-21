#PERGUNTA 1 - Qual é a distribuição das idades dos pacientes e em qual idade há maior ocorrência de doença cardíaca?
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

#Primeiro vamos olhar para as idades dos pacientes

df_2 = pd.read_csv("df_2.csv")

plt.figure(figsize=(8,5))

plt.hist(df_2["Idade"], bins=15, edgecolor="black")

plt.title("Distribuição das idades dos pacientes")
plt.xlabel("Idade (anos)")
plt.ylabel("Número de pacientes")
plt.xticks(np.arange(25, 75 + 1, 5))
plt.show()
