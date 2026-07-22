#3 - Colesterol elevado, pressão arterial elevada e glicemia elevada são doenças relacionadas com a idade?

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

df_2 = pd.read_csv("df_2.csv")

df_2["colesterol_bin"] = (df_2["Colesterol"] > 240).astype(int)

df_2["pressao_bin"] = (df_2["Pressão_Arterial"] > 140).astype(int)

plt.figure(figsize=(8,5))

idade_glicemia_alta = df_2[df_2["Glicemia_bin"] == 1]["Idade"]
idade_pressao_alta = df_2[df_2["pressao_bin"] == 1]["Idade"]
idade_colesterol_alta = df_2[df_2["colesterol_bin"] == 1]["Idade"]


plt.hist(idade_glicemia_alta, bins=10, alpha=1, label="glicemia",edgecolor="gray" )

plt.hist(idade_pressao_alta, bins=10, alpha=0.5, label="pressao",edgecolor="gray")


plt.hist(idade_colesterol_alta, bins=10, alpha=0.2, label="colesterol",edgecolor="gray")

plt.title("Distribuição das idades dos pacientes com doença cardíaca por sexo")
plt.xlabel("Idade (anos)")
plt.ylabel("Número de pacientes")
plt.legend()

plt.show()
