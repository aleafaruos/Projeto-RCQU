#Quantos desses pacientes realmente tiveram o diagnóstico de doença cardiáca?

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

df_2 = pd.read_csv("df_2.csv")
contagem = df_2["Doença_Cardíaca"].value_counts()
print (contagem)

contagem = df_2["Doença_Cardíaca"].value_counts()
print(contagem)

plt.figure(figsize=(8,5))
plt.bar(["Com doença", "Sem doença"], contagem)
plt.title("Distribuição dos pacientes quanto à presença de doença cardíaca")
plt.xlabel("Diagnóstico")
plt.ylabel("Número de pacientes")
plt.show()

