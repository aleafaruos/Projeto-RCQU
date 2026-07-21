### **2 -** Homens e mulheres apresentam a mesma frequência de doença cardíaca e na mesma idade?
#primeiro visualizamos a quantidade de homens e mulheres com doença cardíaca, separadamente


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

df_2 = pd.read_csv("df_2.csv")

df_doenca = df_2[df_2["Doença_Cardíaca"] == 1]
sexo_doenca = df_doenca["Sexo"].value_counts()
print(sexo_doenca)

plt.bar(["M", "F"], sexo_doenca)
plt.xlabel("Sexo")
plt.ylabel("Número de pacientes com doença cardíaca")
plt.title("Distribuição de doença cardíaca por sexo")
plt.show()