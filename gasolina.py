import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dt = pd.read_csv('gasolina.csv', sep=',')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Primeiro gráfico: Lineplot
sns.lineplot(data=dt, x="dia", y="venda", ax=axes[0])
axes[0].set_title("Lineplot das vendas por dia")

# Segundo gráfico: Barplot
sns.barplot(data=dt,x="dia", y="venda", hue="venda", palette="pastel", ax=axes[1])
axes[1].set_title("Barplot das vendas por dia")


fig.savefig("gasolina.png", dpi=300)
plt.tight_layout()
plt.show()
