import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
dt = pd.read_csv('gasolina.csv', sep=',')
x = dt.dia
y = dt.venda

# Criar subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico 1: Usando matplotlib
axes[0].plot(x, y, linestyle="--", label="Preço")
axes[0].fill_between(x, y, color="blue", alpha=0.2)
axes[0].grid(True)
axes[0].set_title('Preço da Gasolina')
axes[0].set_xlabel('Dia')
axes[0].set_ylabel('Preço')
axes[0].legend()

# Gráfico 2: Usando seaborn
sns.lineplot(x=x, y=y, ax=axes[1], label="Preço")
axes[1].grid(True)
axes[1].set_title('Preço da Gasolina')
axes[1].set_xlabel('Dia')
axes[1].set_ylabel('Preço')
axes[1].legend()

# Salvar antes de mostrar
plt.tight_layout()
plt.savefig('gasolina.png')
plt.show()
