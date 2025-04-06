import pandas as pd

def extract_data(filepath):
    """
    Extrai dados de um arquivo CSV e retorna um DataFrame do pandas.
    
    Parâmetros:
    - filepath: caminho para o arquivo CSV

    Retorna:
    - DataFrame com os dados extraídos
    """
    try:
        df = pd.read_csv(filepath)
        print("✅ Dados extraídos com sucesso!")
        return df
    except Exception as e:
        print(f"❌ Erro ao extrair os dados: {e}")
        return None
