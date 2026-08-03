import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Criando o DataFrame com dados aleatórios para simulação
np.random.seed(42)
dados = {
    'Idade': np.random.randint(22, 60, 100),
    'Salario': np.random.normal(5000, 1500, 100).round(2),
    'Anos_Experiencia': np.random.randint(0, 35, 100)
}
df = pd.DataFrame(dados)

# Criando múltiplos gráficos (subplots)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Dispersão - Idade vs Salário
df.plot.scatter(x='Idade', 
                y='Salario', 
                ax=ax1,
                alpha=0.6,
                color='darkblue',
                title='Relação Idade vs Salário',
                xlabel='Idade (anos)',
                ylabel='Salário (R$)',
                s=50)  # Tamanho dos pontos

# Gráfico 2: Histograma - Distribuição de Salários
df['Salario'].plot.hist(ax=ax2,
                       bins=15,
                       color='skyblue',
                       edgecolor='black',
                       title='Distribuição dos Salários',
                       xlabel='Salário (R$)',
                       ylabel='Frequência',
                       alpha=0.7)

# Ajustando os subplots
ax2.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Gráfico 3: Boxplot da experiência por faixa etária (adicional)
fig, ax = plt.subplots(figsize=(10, 6))

# Criando faixas etárias
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=[20, 30, 40, 50, 60], 
                            labels=['20-30', '30-40', '40-50', '50-60'])

df.boxplot(column='Anos_Experiencia', by='Faixa_Etaria', ax=ax)
ax.set_title('Experiência por Faixa Etária')
ax.set_xlabel('Faixa Etária')
ax.set_ylabel('Anos de Experiência')
plt.suptitle('')  # Remove o título automático
plt.show()