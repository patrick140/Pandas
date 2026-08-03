import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
dados = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas_2024': [1200, 1350, 1100, 1500, 1800, 2100],
    'Vendas_2025': [1400, 1600, 1450, 1900, 2200, 2500]
}
df = pd.DataFrame(dados)

# Criando o gráfico de linha
df.plot(x='Mes', 
        y=['Vendas_2024', 'Vendas_2025'], 
        marker='o',
        title='Comparação de Vendas por Mês',
        xlabel='Mês',
        ylabel='Vendas (R$)',
        figsize=(10, 6),
        grid=True)

plt.legend(title='Ano')
plt.show()