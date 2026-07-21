import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit



#visualizando as colunas presentes no dataset
df = pd.read_csv("dados.csv") 
print(df.columns.tolist())

df = df.rename(columns={
    "Age": "Idade",
    "Sex": "Sexo",
    "ChestPainType": "ChestPainType",
    "RestingBP": "Pressão_Arterial",
    "Cholesterol": "Colesterol",
    "FastingBS": "Glicemia_bin",
    "RestingECG": "RestingECG",
    "MaxHR": "Freq_max",
    "ExerciseAngina": "ExerciseAngina",
    "Oldpeak": "Oldpeak",
    "ST_Slope": "ST_Slope",
    "HeartDisease": "Doença_Cardíaca"
})

#excluindo colunas desnecessárias
df.drop(columns=['ChestPainType','RestingECG','ExerciseAngina', 'Oldpeak', 'ST_Slope'], inplace=True)

print(df.columns.tolist())

#redefinindo minha lista para as novas colunas e para dados do colesterol diferentes de 0
df_2 = df[df["Colesterol"] != 0]

#criando outro dataframe com os dados já limpos para serem acessado nas análises
df_2.to_csv("df_2.csv", index=False)