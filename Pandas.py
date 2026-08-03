import pandas as pd 
import matplotlib.pyplot as plt 
 
# Cria um DataFrame de exemplo 
dados = { 
   'Ano': [2019, 2020, 2021, 2022, 2023], 
   'Vendas': [150, 200, 250, 300, 350] 
} 
df = pd.DataFrame(dados) 
 
# Cria o gráfico de linha (padrão) 
df.plot(x='Ano', y='Vendas', title='Vendas por Ano') 
plt.show()