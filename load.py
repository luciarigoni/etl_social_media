def load_data(df, output_path):
    """
    Salva o DataFrame transformado em um arquivo CSV.

    Parâmetros:
    - df: DataFrame do pandas
    - output_path: caminho de destino do arquivo CSV
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"📦 Dados salvos com sucesso em: {output_path}")
    except Exception as e:
        print(f"❌ Erro ao salvar os dados: {e}")
