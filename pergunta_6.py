import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

df_2 = pd.read_csv("df_2.csv")

df_2["colesterol_bin"] = (df_2["Colesterol"] > 240).astype(int)

df_2["pressao_bin"] = (df_2["Pressão_Arterial"] > 140).astype(int)

df_2["NumFatoresRisco"] = (df_2["colesterol_bin"] + df_2["pressao_bin"] + df_2["Glicemia_bin"])

tabela = pd.crosstab(df_2["NumFatoresRisco"], df_2["Doença_Cardíaca"], normalize="index")

tabela.plot(kind="bar", stacked=True)
plt.xticks(rotation=0)
plt.xlabel("Número de fatores de risco")
plt.ylabel("Proporção")
plt.title("Doença cardíaca por número de fatores de risco")
plt.show()