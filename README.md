# Projeto-RCQU

análise exploratória de dados de colesterol e fatores de risco cardíaco, dataset do Kaggle. Esse trabalho teve como objetivo o aprofundamento das funções do Pandas e sql e para isso foram usadas dados de riscos cardiacos retirados do Kaggle onde fora feita a limpeza de dados, retirando as linhas de valores faltantes e colunas que não foram análisadas, para posteriormente respondermos algumas perguntas relacionadas as correlações dos dados ou extrair inferencias dos dados.

## Estrutura do projeto

```
projetohd/
├── dados.csv         
├── df_2.csv          
├── limpeza.py         
├── pergunta_1_a.py
├── pergunta_1_b.py
├── pergunta_1_c.py
├── pergunta_2_a.py
├── pergunta_2_b.py
├── pergunta_3.py
├── pergunta_4.py
├── pergunta_5.py
├── requirements.txt
└── README.md
```

## Fonte dos dados

Dataset público retirado do Kaggle: [nome do dataset](link-do-kaggle-aqui).

## Como rodar o projeto

1. Clone o repositório:
```bash
   git clone https://github.com/aleafaruos/Projeto-RCQU
   cd projeto-RCQU
```

2. Crie um ambiente virtual e instale as dependências:
```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
```

3. Rode o script de limpeza:
```bash
   python src/limpeza.py
```
   Isso vai gerar o arquivo `data/processed/df_2.csv` a partir do dado bruto em `data/raw/`.

4. Use o dado processado (`df_2.csv`) nas análises/notebooks.



## Autores

<div align="center">

| <a href="https://github.com/aleafaruos"><img src="https://github.com/aleafaruos.png" width="80" style="border-radius:50%"></a> | <a href="https://github.com/lucashc-c"><img src="https://github.com/lucashc-c.png" width="80" style="border-radius:50%"></a> |
|:---:|:---:|
| Dimadim | Luquinhas |

</div>





