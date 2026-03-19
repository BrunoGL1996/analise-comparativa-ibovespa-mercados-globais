import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- 1. CONFIGURAÇÕES E COLETA DE DADOS ---
# Definindo os índices (Brasil, EUA, China, Rússia)
tickers = ["^BVSP", "^GSPC", "000001.SS", "IMOEX.ME"]

print("📊 Coletando dados reais do mercado...")
# Coleta dos preços de fechamento dos últimos 2 anos
dados = yf.download(tickers, period="2y")['Close']

# --- 2. TRATAMENTO E NORMALIZAÇÃO ---
# Normalização para Base 100 para comparar performance relativa
# (valor atual / valor inicial) * 100
dados_norm = (dados / dados.iloc[0]) * 100

# Exportando os dados tratados para CSV
dados_norm.to_csv("analise_geopolitica_bolsas.csv")

# --- 3. VISUALIZAÇÃO: PERFORMANCE ACUMULADA ---
plt.figure(figsize=(12, 6))
plt.plot(dados_norm['^BVSP'], label='Ibovespa (Brasil)', color='green', linewidth=1.5)
plt.plot(dados_norm['^GSPC'], label='S&P 500 (EUA)', color='blue', linewidth=1.5)
plt.plot(dados_norm['000001.SS'], label='SSE Composite (China)', color='orange', linewidth=1.5)
plt.plot(dados_norm['IMOEX.ME'], label='MOEX (Russia)', color='red', linewidth=1.5)

plt.title('Performance Acumulada: Impacto Global nas Principais Bolsas\n(Brasil, EUA, China e Rússia - Últimos 24 meses)', fontsize=14)
plt.xlabel('Data')
plt.ylabel('Base 100')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout() # Ajusta o layout para não cortar textos
plt.show()

# --- 4. ANÁLISE DE CORRELAÇÃO ---
# Calculando a matriz de correlação de retornos diários
# (Melhor prática: correlação sobre o retorno, não sobre o preço bruto)
retornos = dados.pct_change()
correlacao = retornos.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlacao,
    annot=True,
    cmap='RdYlGn',
    vmin=-1,
    vmax=1,
    fmt=".2f",
    linewidths=0.5
)

plt.title('Matriz de Correlação de Retornos: Brasil vs Mundo', fontsize=14)
plt.tight_layout()
plt.show()