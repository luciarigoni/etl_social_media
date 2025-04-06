from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    # Caminho para o CSV na pasta raw
    filepath = "data/raw/Viral_Social_Media_Trends.csv"

    # Executa a etapa de extração
    df = extract_data(filepath)

    # Visualiza as primeiras linhas e extrai informações
    if df is not None:
        df = transform_data(df)
        print(df.head())
    output_path = "data/processed/viral_trends_clean.csv"
    load_data(df, output_path)

if __name__ == "__main__":
    main()
