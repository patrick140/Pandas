import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("Vendas_mês.csv")
print(df)

df.plot(x='Mês', 
        y=["Vendas_Produto_A", "Vendas_Produto_B", "Vendas_Produto_C"],
        kind='line',
        marker='o',           # Adiciona marcadores
        markersize=8,         # Tamanho dos marcadores
        linewidth=2.5,        # Espessura das linhas
        title='Vendas por Mês - 2024',
        grid=True,
        legend=True)
 
plt.show()



