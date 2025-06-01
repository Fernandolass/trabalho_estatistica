# Análise de Temperaturas Globais

Este programa realiza uma análise das temperaturas globais ao longo do tempo, incluindo:
- Cálculo da média anual das temperaturas
- Visualização da tendência das temperaturas por décadas
- Análise da variação sazonal das temperaturas

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python listadas em `requirements.txt`
- Conta no Kaggle (para download automático do dataset)

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração do Kaggle

Para permitir o download automático do dataset, você precisa configurar suas credenciais do Kaggle:

1. Acesse sua conta no Kaggle
2. Vá para "Account" (canto superior direito)
3. Role até "API" e clique em "Create New API Token"
4. Isso irá baixar um arquivo `kaggle.json`
5. Coloque este arquivo em `~/.kaggle/kaggle.json` (Linux/Mac) ou `C:\Users\<Windows-username>\.kaggle\kaggle.json` (Windows)

## Uso

Execute o programa:
```bash
python analise_temperaturas.py
```

O programa irá:
- Baixar automaticamente o dataset do Kaggle (se não estiver presente)
- Exibir a média anual das temperaturas no console
- Gerar dois arquivos de gráfico:
  - `tendencia_decadas.png`: Mostra a tendência das temperaturas por décadas
  - `variacao_sazonal.png`: Mostra a variação sazonal das temperaturas

## Dataset

O programa utiliza o dataset "Climate Change: Earth Surface Temperature Data" do Kaggle, que será baixado automaticamente na primeira execução. 