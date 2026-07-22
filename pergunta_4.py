#3- Como a frequência cardíaca máxima varia com a idade?

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df_2 = pd.read_csv("df_2.csv")

plt.figure(figsize=(8,5))

df_sem = df_2[df_2["Doença_Cardíaca"] == 0]
df_com = df_2[df_2["Doença_Cardíaca"] == 1]

plt.scatter(df_sem["Idade"], df_sem["Freq_max"], alpha=1, label="Sem doença")

plt.scatter(df_com["Idade"], df_com["Freq_max"], alpha=1, label="Com doença")

plt.title("Relação entre idade e frequência cardíaca máxima por diagnóstico")
plt.xlabel("Idade (anos)")
plt.ylabel("Frequência cardíaca máxima (bpm)")
plt.legend()

plt.show()
