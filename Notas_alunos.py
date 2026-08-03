import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
dados = {
    'Aluno': ['Ana', 'Carlos', 'Mariana', 'Pedro', 'Julia'],
    'Matemática': [8.5, 7.0, 9.5, 6.5, 9.0],
    'Português': [9.0, 6.5, 8.0, 7.5, 8.5],
    'Ciências': [7.5, 8.0, 9.0, 7.0, 9.5]
}
df = pd.DataFrame(dados)

# Criando o gráfico de barras agrupadas
df.set_index('Aluno').plot(kind='bar', 
                           figsize=(12, 6),
                           title='Notas dos Alunos por Disciplina',
                           xlabel='Aluno',
                           ylabel='Nota',
                           rot=0,  # Rotação das labels
                           colormap='viridis',
                           edgecolor='black')

plt.legend(title='Disciplina', loc='upper right')
plt.grid(axis='y', alpha=0.3)
plt.show()