import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import kagglehub
import os

# Configuração do estilo dos gráficos
plt.style.use('seaborn-v0_8')  # Corrigindo o estilo do seaborn
sns.set_theme()  # Usando o tema padrão do seaborn

def baixar_dataset():
    """
    Baixa o dataset do Kaggle usando kagglehub.
    Retorna o caminho para o arquivo do dataset.
    """
    print("Baixando dataset do Kaggle...")
    path = kagglehub.dataset_download("berkeleyearth/climate-change-earth-surface-temperature-data")
    print(f"Dataset baixado com sucesso em: {path}")
    return path

def carregar_dados():
    """
    Carrega e prepara os dados de temperatura.
    Retorna um DataFrame com os dados processados.
    """
  
    if not os.path.exists('GlobalLandTemperaturesByCountry.csv'):
        path = baixar_dataset()
     
        import shutil
        shutil.copy(os.path.join(path, 'GlobalLandTemperaturesByCountry.csv'), '.')
 

    df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
    
    
    df['dt'] = pd.to_datetime(df['dt'])
    
    # Extraindo ano e mês
    df['ano'] = df['dt'].dt.year
    df['mes'] = df['dt'].dt.month
    
    return df

def calcular_media_anual(df):
    """
    Calcula a média anual das temperaturas globais.
    """
    media_anual = df.groupby('ano')['AverageTemperature'].mean().reset_index()
    return media_anual

def plotar_tendencia_decadas(df):
    """
    Plota a tendência das temperaturas ao longo das décadas.
    """
    
    df['decada'] = (df['ano'] // 10) * 10
    media_decadas = df.groupby('decada')['AverageTemperature'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(media_decadas['decada'], media_decadas['AverageTemperature'], 
             marker='o', linewidth=2, markersize=8)
    plt.title('Tendência das Temperaturas Globais por Década')
    plt.xlabel('Década')
    plt.ylabel('Temperatura Média (°C)')
    plt.grid(True)
    plt.savefig('tendencia_decadas.png')
    plt.close()

def analisar_variacao_sazonal(df):
    """
    Analisa a variação sazonal das temperaturas.
    """
    
    media_mensal = df.groupby('mes')['AverageTemperature'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(media_mensal['mes'], media_mensal['AverageTemperature'], 
             marker='o', linewidth=2, markersize=8)
    plt.title('Variação Sazonal das Temperaturas Globais')
    plt.xlabel('Mês')
    plt.ylabel('Temperatura Média (°C)')
    plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
    plt.grid(True)
    plt.savefig('variacao_sazonal.png')
    plt.close()

def main():
    
    print("Carregando dados...")
    df = carregar_dados()
    
    
    print("\nCalculando média anual...")
    media_anual = calcular_media_anual(df)
    print("\nMédia anual das temperaturas globais:")
    print(media_anual.tail())
    
    
    print("\nGerando gráfico de tendência por décadas...")
    plotar_tendencia_decadas(df)
    
    
    print("\nAnalisando variação sazonal...")
    analisar_variacao_sazonal(df)
    
    print("\nAnálise concluída! Os gráficos foram salvos como 'tendencia_decadas.png' e 'variacao_sazonal.png'")

if __name__ == "__main__":
    main() 