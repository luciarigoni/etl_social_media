# ETL Project - Viral Social Media Trends Analysis

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para processar e analisar dados de tendências virais em redes sociais.

## Estrutura do Projeto

```
etl_project/
├── data/
│   ├── raw/         # Dados brutos
│   └── processed/   # Dados processados
├── extract.py       # Módulo de extração de dados
├── transform.py     # Módulo de transformação de dados
├── load.py         # Módulo de carregamento de dados
└── main.py         # Script principal
```

## Descrição

O projeto processa dados de tendências virais em redes sociais através de três etapas principais:

1. **Extração (Extract)**:

   - Lê dados do arquivo CSV fonte
   - Realiza validações iniciais dos dados

2. **Transformação (Transform)**:

   - Limpa e processa os dados
   - Aplica transformações necessárias
   - Prepara os dados para análise

3. **Carregamento (Load)**:
   - Salva os dados processados em um novo arquivo CSV
   - Mantém os dados originais intactos

## Requisitos

- Python 3.x
- pandas
- numpy

## Como Usar

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```

## Estrutura de Dados

O projeto trabalha com dados de tendências virais em redes sociais, processando:

- Dados brutos do arquivo: `data/raw/Viral_Social_Media_Trends.csv`
- Dados processados salvos em: `data/processed/viral_trends_clean.csv`

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests ou reportando issues.

## Licença

Este projeto está sob a licença MIT.
