import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Carregamento do dataset
url = "https://raw.githubusercontent.com/Fernandolass/trabalho_q06/main/trabalho_q06/AirQuality.csv"
df = pd.read_csv(url, sep=';', decimal=',')


# 2. Pré-processamento
df = df.replace(-200, np.nan)
df = df.dropna(axis=1, thresh=len(df)*0.8)  # Remove colunas com mais de 20% de valores faltantes
df = df.dropna()  # Remove linhas com valores faltantes

# 3. Medidas descritivas
estatisticas = df.describe()
print("Medidas estatísticas descritivas:")
print(estatisticas)

# 4. Visualizações
plt.figure(figsize=(12, 5))
sns.histplot(df["CO(GT)"], kde=True)
plt.title("Distribuição de CO (monóxido de carbono)")
plt.xlabel("CO(GT)")
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x=df["NO2(GT)"])
plt.title("Boxplot de NO2")
plt.show()

# 5. Correlação entre CO e NO2
sns.scatterplot(x="CO(GT)", y="NO2(GT)", data=df)
plt.title("Dispersão: CO vs NO2")
plt.show()

# 6. Regressão linear simples (CO vs NO2)
X = df[["CO(GT)"]]
y = df["NO2(GT)"]
modelo = LinearRegression()
modelo.fit(X, y)

print(f"Coeficiente angular (inclinação): {modelo.coef_[0]:.4f}")
print(f"Coeficiente linear (intercepto): {modelo.intercept_:.4f}")
print(f"R²: {modelo.score(X, y):.4f}")

# 7. Teste de hipótese (t-test entre médias de NO2 antes e depois de certo nível de CO)
grupo1 = df[df["CO(GT)"] <= 2]["NO2(GT)"]
grupo2 = df[df["CO(GT)"] > 2]["NO2(GT)"]
t_stat, p_valor = stats.ttest_ind(grupo1, grupo2)

print(f"\nTeste t entre grupos de NO2 com CO baixo vs alto:")
print(f"T-statística = {t_stat:.4f}")
print(f"Valor-p = {p_valor:.4f}")
