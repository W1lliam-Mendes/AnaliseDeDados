import pandas as pd
import plotly.express as px

df = pd.read_excel("Vendas.xlsx")
df = df.dropna()

display(df.head())

#=================================#

faturamentoTotal = df["Valor Final"].sum()
print(faturamentoTotal)

#=================================#

faturamentoLoja = df[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamentoLoja)

#=================================#

faturamentoProduto = df[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamentoProduto)

#=================================#

