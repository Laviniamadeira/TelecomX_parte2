# 📞 TelecomX - Análise Preditiva de Evasão de Clientes



## 📊 Sobre o Projeto

O **TelecomX** é um projeto completo de **Machine Learning** focado na **previsão de evasão de clientes (churn)** em uma empresa de telecomunicações. Utilizando técnicas avançadas de ciência de dados, o projeto desenvolve modelos preditivos capazes de identificar clientes com alto risco de cancelamento, permitindo ações proativas de retenção.

### 🎯 Problema de Negócio

Com uma taxa de evasão atual de **25.72%**, a empresa precisa identificar os fatores que mais influenciam o cancelamento de serviços e desenvolver estratégias eficazes de retenção de clientes.

## 🏆 Resultados Principais

- **4 modelos** de machine learning desenvolvidos e avaliados
- **Melhor modelo:** Regressão Logística com **F1-Score de 0.5795**
- **Principais fatores de churn identificados:**
  - Tempo como cliente (fator de proteção)
  - Tipo de internet Fiber Optic (fator de risco)
  - Custo total (fator de risco)

## 🧰 Tecnologias Utilizadas

### Linguagens e Bibliotecas
- **Python 3.8+**
- **Pandas** - Manipulação de dados
- **NumPy** - Operações numéricas
- **Scikit-learn** - Machine Learning
- **Seaborn/Matplotlib** - Visualizações
- **Warnings** - Controle de avisos

### Modelos de Machine Learning
- **Regressão Logística** ⭐ (Melhor performance)
- **Random Forest**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**

## 📁 Estrutura do Projeto

```
TelecomX/
├── README.md                    # Documentação do projeto
├── TelecomX_parte2.ipynb       # Notebook principal com análises
├── dados_limpos.csv            # Dataset processado

```

## 📋 Funcionalidades Implementadas

### 🔧 Pré-processamento de Dados
- Limpeza e tratamento de dados ausentes
- Conversão de variáveis categóricas (One-Hot Encoding)
- Normalização de dados para modelos sensíveis à escala
- Criação de variáveis derivadas (`contas_diarias`)

### 📊 Análise Exploratória
- Análise de correlações entre variáveis
- Visualizações estatísticas avançadas
- Identificação de padrões de comportamento
- Análise da distribuição de churn

### 🤖 Modelagem Preditiva
- **Pipeline completo** de Machine Learning
- **Validação cruzada** estratificada (70/30)
- **Avaliação robusta** com múltiplas métricas:
  - Accuracy, Precision, Recall, F1-Score
  - Matrizes de confusão
  - Análise de overfitting/underfitting

### 🔍 Interpretabilidade
- **Importância das features** (Random Forest)
- **Análise de coeficientes** (Regressão Logística)
- **Insights estratégicos** para tomada de decisão

## 📊 Principais Descobertas

### 🎯 Fatores de Risco (Aumentam Churn)
1. **Fibra Óptica:** Clientes com internet fibra têm maior propensão ao cancelamento
2. **Alto Custo Total:** Clientes que gastam mais tendem a cancelar
3. **Método de Pagamento:** Cheque eletrônico aumenta risco

### 🛡️ Fatores de Proteção (Diminuem Churn)
1. **Tempo de Relacionamento:** Clientes antigos são mais fiéis
2. **Contratos de 2 anos:** Maior estabilidade
3. **Múltiplos Serviços:** Clientes com mais serviços cancelam menos

## 🚀 Como Executar o Projeto

### Pré-requisitos
```bash
pip install pandas numpy scikit-learn seaborn matplotlib
```

### Execução
1. Clone o repositório
2. Abra o notebook `TelecomX_parte2.ipynb`
3. Execute as células sequencialmente
4. Analise os resultados e visualizações

## 📈 Métricas de Performance

| Modelo | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| **Regressão Logística** ⭐ | **0.8010** | **0.6348** | **0.5330** | **0.5795** |
| Random Forest | 0.7762 | 0.5867 | 0.4403 | 0.5031 |
| KNN | 0.7634 | 0.5455 | 0.4813 | 0.5114 |
| SVM | 0.7937 | 0.6300 | 0.4795 | 0.5445 |

## 💡 Insights Estratégicos

### Para o Negócio
- **Taxa atual de churn:** 25.72%
- **Potencial de identificação:** 58% dos casos de churn
- **ROI esperado:** Redução significativa na perda de clientes

### Recomendações
1. **Programas de fidelidade** para clientes novos (< 12 meses)
2. **Revisão de preços** para serviços de fibra óptica
3. **Incentivos** para contratos de longo prazo
4. **Melhoria** nos métodos de pagamento


## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novas funcionalidades
- Otimizar algoritmos

