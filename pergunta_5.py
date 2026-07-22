#5 - Glicemia, Pressão e Colesterol estão relacionadas entre si e com doencas cardiacas?

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df_2 = pd.read_csv("df_2.csv")

df_2["colesterol_bin"] = (df_2["Colesterol"] > 240).astype(int)

df_2["pressao_bin"] = (df_2["Pressão_Arterial"] > 140).astype(int)

dados = df_2[['pressao_bin', 'colesterol_bin', "Glicemia_bin", 'Doença_Cardíaca' ]]

corr = dados.corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlação entre colesterol, pressão arterial, glicemia e doença cardiaca")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.show()
