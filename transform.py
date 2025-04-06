def transform_data(df):
    """
    Aplica transformações no DataFrame:
    - Padroniza colunas de texto (minúsculas, sem espaços)
    - Cria nova coluna de taxa de engajamento

    Retorna:
    - DataFrame transformado
    """
    # Padronizar colunas de texto
    text_columns = ['Platform', 'Hashtag', 'Content_Type', 'Region', 'Engagement_Level']
    df[text_columns] = df[text_columns].apply(lambda col: col.str.strip().str.lower())

    # Criar coluna de taxa de engajamento
    df["Engagement_Rate"] = (df["Likes"] + df["Shares"] + df["Comments"]) / df["Views"]

    print("🔧 Transformações aplicadas com sucesso!")
    return df
