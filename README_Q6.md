# Análise da Qualidade do Ar – Questão 06 📊🌫️

Este projeto realiza uma análise estatística do conjunto de dados **Air Quality UCI**, com foco na avaliação da relação entre os poluentes **CO(GT)** e **NO₂(GT)**. Trata-se de uma atividade da disciplina de Estatística (Unidade II), utilizando Python para visualização, modelagem e inferência estatística.

---

## 🧪 Técnicas Utilizadas

- Estatísticas descritivas (`mean`, `std`, `min`, `max`, `quartis`)
- Visualizações gráficas:
  - Histograma (CO)
  - Boxplot (NO₂)
  - Gráfico de dispersão
- Regressão linear simples
- Teste de hipótese (t de Student para duas amostras independentes)

---

## 📁 Estrutura do Repositório

```
trabalho_q06/
│
├── AirQuality.csv              
├── trabalho_estatistica.py      
└── README.md                    
```

---

## ▶️ Como Executar

### 1. Clone este repositório
```bash
git clone https://github.com/Fernandolass/trabalho_q06.git
cd trabalho_q06
```

### 2. (Recomendado) Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o código
```bash
python trabalho_estatistica.py
```

---

## 📚 Requisitos

Este projeto requer Python 3.7+ e as seguintes bibliotecas:

- pandas
- seaborn
- matplotlib
- scipy
- scikit-learn
- numpy

---

## 👥 Integrantes do Grupo 6

- Fernando Santana  
- Manoel Eduardo  
- Carlos Diego  
- Igor Barreto  
- Kayky Lima  
- Fabiano Vidal  
- Irwing Arrius  

---

## 🎓 Professor

Carlos Gustavo – Disciplina de Estatística

---

## 🔗 Dataset

[Air Quality UCI Dataset (original)](https://archive.ics.uci.edu/ml/datasets/Air+quality)

---
