from utils import load_datasets, convert_dates, filter_dataframes, resample_dataframes, create_grafico_general, plot_company_close_evolution, merge_dataframes

# Cargar los datasets
apple, amazon, google, meta, microsoft, nvidia, tesla = load_datasets()

# Crear diccionario con los DataFrames
dataframes_dict = {
    'apple': apple,
    'amazon': amazon,
    'google': google,
    'meta': meta,
    'microsoft': microsoft,
    'nvidia': nvidia,
    'tesla': tesla
}

# Convertir las fechas a formato datetime
dataframes_dict = convert_dates(dataframes_dict)

# Filtrar los DataFrames (solo 'Date', 'Open', 'High', 'Low', 'Close')
filtered_dataframes = filter_dataframes(dataframes_dict)

# Resumir por mes y año
monthly_dataframes = resample_dataframes(filtered_dataframes, 'M')
annual_dataframes = resample_dataframes(filtered_dataframes, 'Y')

# Crear gráficos generales
apple_grafico_general = create_grafico_general(annual_dataframes['apple'], 'Close', 'AAPL')
amazon_grafico_general = create_grafico_general(annual_dataframes['amazon'], 'Close', 'AMZN')

# Graficar la evolución de los precios de cierre
plot_company_close_evolution(apple_grafico_general, 'AAPL')
plot_company_close_evolution(amazon_grafico_general, 'AMZN')

# Unir los DataFrames para un gráfico combinado
merged_df = merge_dataframes([apple_grafico_general, amazon_grafico_general])

# Mostrar resultados
print(merged_df.head())
