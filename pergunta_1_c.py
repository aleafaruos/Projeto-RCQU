#Finalmente conseguimos responder a pergunta, sobre a idade dos pacientes que possuem doença.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df_2 = pd.read_csv("df_2.csv")

plt.figure(figsize=(8,5))

idade_sem = df_2[df_2["Doença_Cardíaca"] == 0]["Idade"]
idade_com = df_2[df_2["Doença_Cardíaca"] == 1]["Idade"]

plt.hist(idade_sem, bins=15, alpha=0.6, label="Sem doença", edgecolor="gray")
plt.hist(idade_com, bins=15, alpha=0.45, label="Com doença", edgecolor="gray")
plt.title("Distribuição das idades por diagnóstico")
plt.xlabel("Idade (anos)")
plt.ylabel("Número de pacientes")
plt.legend()
plt.show()
