import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3


df_2 = pd.read_csv("df_2.csv")
conexao = sqlite3.connect("dados_doencas.db")
df_2.to_sql("pacientes", conexao, if_exists="replace", index=False)

idade_sem_sql = pd.read_sql("""
SELECT Idade
FROM pacientes
WHERE Doença_Cardíaca = 0
""", conexao)

idade_com_sql = pd.read_sql("""
SELECT Idade
FROM pacientes
WHERE Doença_Cardíaca = 1
""", conexao)

print('Usando o pandas')
print(type(idade_com))
print(idade_com)
print('Usando SQL')
print(type(idade_com_sql))
print(idade_com_sql)

# segundo bloco

onexao = sqlite3.connect("dados_doencas.db")
criar_coluna = """
SELECT
    Idade,
    Doença_Cardíaca,
    Glicemia_bin,
    CASE
        WHEN Colesterol > 240 THEN 1
        ELSE 0
    END AS colesterol_bin,

    CASE
        WHEN Pressão_Arterial > 140 THEN 1
        ELSE 0
    END AS pressao_bin

FROM pacientes;
"""

idade_glicemia_alta_sq = pd.read_sql("""
SELECT Idade
FROM pacientes
WHERE Glicemia_bin = 1;
""", conexao)["Idade"]

idade_pressao_alta_sq = pd.read_sql("""
SELECT Idade
FROM pacientes
WHERE Pressão_Arterial > 140;
""", conexao)["Idade"]

idade_colesterol_alta_sq = pd.read_sql("""
SELECT Idade
FROM pacientes
WHERE Colesterol > 240;
""", conexao)["Idade"]


# O plot foi feito da mesma forma

plt.figure(figsize=(8,5))
plt.hist(idade_glicemia_alta_sq, bins=10, alpha=1, label="Glicemia alta", edgecolor="gray")
plt.hist(idade_pressao_alta_sq, bins=10, alpha=0.5,label="Pressão alta",edgecolor="gray")
plt.hist(idade_colesterol_alta_sq, bins=10,alpha=0.2,label="Colesterol alto", edgecolor="gray")
plt.title("Distribuição das idades por fator de risco")
plt.xlabel("Idade (anos)")
plt.ylabel("Número de pacientes")
plt.legend()
plt.show()

