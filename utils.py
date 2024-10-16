apple = pd.read_csv("Datasets/AAPL1424.csv")
amazon = pd.read_csv("Datasets/AMZN1424.csv")
google = pd.read_csv("Datasets/GOOGL1424.csv")
meta = pd.read_csv("Datasets/META1424.csv")
microsoft = pd.read_csv("Datasets/MSFT1424.csv")
nvidia = pd.read_csv("Datasets/NVDA1424.csv")
tesla = pd.read_csv("Datasets/TSLA1424.csv")



# Eliminar la columna 'Unnamed: 0' de todos los DataFrames
dataframes = [apple, amazon, google, meta, microsoft, nvidia, tesla]

for df in dataframes:
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

# Mostrar las primeras filas para verificar que se haya eliminado la columna
for df_name, df in zip(['apple', 'amazon', 'google', 'meta', 'microsoft', 'nvidia', 'tesla'], dataframes):
    print(f"Primeras filas de {df_name}:")
    print(df.head(), "\n")



# Crear un diccionario con los nombres y DataFrames
dataframes_dict = {
    'apple': apple,
    'amazon': amazon,
    'google': google,
    'meta': meta,
    'microsoft': microsoft,
    'nvidia': nvidia,
    'tesla': tesla
}

# Convertir la columna de fechas a formato datetime para cada DataFrame
for name, df in dataframes_dict.items():
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Verificar que la columna 'Date' se ha convertido correctamente
date_info = {name: df['Date'].dtype for name, df in dataframes_dict.items()}
date_samples = {name: df['Date'].head() for name, df in dataframes_dict.items()} 



# Crear una nueva versión de cada DataFrame con solo las columnas seleccionadas: 'Date', 'Open', 'High', 'Low', 'Close'
filtered_dataframes = {name: df[['Date', 'Open', 'High', 'Low', 'Close']] for name, df in dataframes_dict.items()}

# Mostrar las primeras filas de cada DataFrame filtrado para confirmar
for name, df in filtered_dataframes.items():
    print(f"Primeras filas del dataset filtrado de {name}:")
    print(df.head(), "\n")



# Crear y asignar nombres a las versiones filtradas de cada DataFrame
apple_filtered = filtered_dataframes['apple']
amazon_filtered = filtered_dataframes['amazon']
google_filtered = filtered_dataframes['google']
meta_filtered = filtered_dataframes['meta']
microsoft_filtered = filtered_dataframes['microsoft']
nvidia_filtered = filtered_dataframes['nvidia']
tesla_filtered = filtered_dataframes['tesla']

# Mostrar las primeras filas de cada DataFrame filtrado para confirmar los resultados
for name, df in zip(['apple_filtered', 'amazon_filtered', 'google_filtered', 'meta_filtered', 
                     'microsoft_filtered', 'nvidia_filtered', 'tesla_filtered'], 
                    [apple_filtered, amazon_filtered, google_filtered, meta_filtered, 
                     microsoft_filtered, nvidia_filtered, tesla_filtered]):
    print(f"Primeras filas del dataset {name}:")
    print(df.head(), "\n")



# Crear versiones resumidas por mes para cada DataFrame filtrado
apple_monthly = apple_filtered.resample('M', on='Date').mean()
amazon_monthly = amazon_filtered.resample('M', on='Date').mean()
google_monthly = google_filtered.resample('M', on='Date').mean()
meta_monthly = meta_filtered.resample('M', on='Date').mean()
microsoft_monthly = microsoft_filtered.resample('M', on='Date').mean()
nvidia_monthly = nvidia_filtered.resample('M', on='Date').mean()
tesla_monthly = tesla_filtered.resample('M', on='Date').mean()

# Mostrar las primeras filas de cada DataFrame resumido para confirmar los resultados
for name, df in zip(['apple_monthly', 'amazon_monthly', 'google_monthly', 'meta_monthly', 
                     'microsoft_monthly', 'nvidia_monthly', 'tesla_monthly'], 
                    [apple_monthly, amazon_monthly, google_monthly, meta_monthly, 
                     microsoft_monthly, nvidia_monthly, tesla_monthly]):
    print(f"Primeras filas del dataset {name}:")
    print(df.head(), "\n")



# Crear versiones resumidas por año para cada DataFrame filtrado
apple_annual = apple_filtered.resample('Y', on='Date').mean()
amazon_annual = amazon_filtered.resample('Y', on='Date').mean()
google_annual = google_filtered.resample('Y', on='Date').mean()
meta_annual = meta_filtered.resample('Y', on='Date').mean()
microsoft_annual = microsoft_filtered.resample('Y', on='Date').mean()
nvidia_annual = nvidia_filtered.resample('Y', on='Date').mean()
tesla_annual = tesla_filtered.resample('Y', on='Date').mean()

# Mostrar las primeras filas de cada DataFrame resumido para confirmar los resultados
for name, df in zip(['apple_annual', 'amazon_annual', 'google_annual', 'meta_annual', 
                     'microsoft_annual', 'nvidia_annual', 'tesla_annual'], 
                    [apple_annual, amazon_annual, google_annual, meta_annual, 
                     microsoft_annual, nvidia_annual, tesla_annual]):
    print(f"Primeras filas del dataset {name}:")
    print(df.head(), "\n")


# crear las tablas de cada compañia con los filtros aplciados para luego graficarlas
def create_grafico_general(df, close_column, company_name):
    company_grafico_general = df[[close_column]].copy()
    company_grafico_general['Year'] = company_grafico_general.index.year
    company_grafico_general = company_grafico_general[['Year', close_column]]
    company_grafico_general.columns = ['Year', f'Close_{company_name}']
    return company_grafico_general

# Aplicar la función para cada compañía
apple_grafico_general = create_grafico_general(apple_annual, 'Close_AAPL', 'AAPL')
amazon_grafico_general = create_grafico_general(amazon_annual, 'Close_AMZN', 'AMZN')
google_grafico_general = create_grafico_general(google_annual, 'Close_GOOGL', 'GOOGL')
meta_grafico_general = create_grafico_general(meta_annual, 'Close_META', 'META')
microsoft_grafico_general = create_grafico_general(microsoft_annual, 'Close_MSFT', 'MSFT')
nvidia_grafico_general = create_grafico_general(nvidia_annual, 'Close_NVDA', 'NVDA')
tesla_grafico_general = create_grafico_general(tesla_annual, 'Close_TSLA', 'TSLA')



# Función para graficar la evolución del 'Close' de una compañía
def plot_company_close_evolution(df, company_name):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df[f'Close_{company_name}'], marker='o', linestyle='-', label=f'Evolución {company_name}')
    plt.title(f'Evolución del precio de cierre de {company_name} desde 2014 hasta la actualidad')
    plt.xlabel('Año')
    plt.ylabel('Precio de Cierre')
    plt.grid(True)
    plt.legend()
    plt.show()

# Graficar la evolución del 'Close' para cada compañía
plot_company_close_evolution(apple_grafico_general, 'AAPL')
plot_company_close_evolution(amazon_grafico_general, 'AMZN')
plot_company_close_evolution(google_grafico_general, 'GOOGL')
plot_company_close_evolution(meta_grafico_general, 'META')
plot_company_close_evolution(microsoft_grafico_general, 'MSFT')
plot_company_close_evolution(nvidia_grafico_general, 'NVDA')
plot_company_close_evolution(tesla_grafico_general, 'TSLA')



# Hacer merge de los DataFrames en base al 'Year'
merged_df = apple_grafico_general.merge(amazon_grafico_general, on='Year') \
                                 .merge(google_grafico_general, on='Year') \
                                 .merge(meta_grafico_general, on='Year') \
                                 .merge(microsoft_grafico_general, on='Year') \
                                 .merge(nvidia_grafico_general, on='Year') \
                                 .merge(tesla_grafico_general, on='Year')

# Graficar todas las compañías en un solo gráfico
plt.figure(figsize=(12, 8))

# Graficar cada compañía
plt.plot(merged_df['Year'], merged_df['Close_AAPL'], marker='o', linestyle='-', label='Apple (AAPL)')
plt.plot(merged_df['Year'], merged_df['Close_AMZN'], marker='o', linestyle='-', label='Amazon (AMZN)')
plt.plot(merged_df['Year'], merged_df['Close_GOOGL'], marker='o', linestyle='-', label='Google (GOOGL)')
plt.plot(merged_df['Year'], merged_df['Close_META'], marker='o', linestyle='-', label='Meta (META)')
plt.plot(merged_df['Year'], merged_df['Close_MSFT'], marker='o', linestyle='-', label='Microsoft (MSFT)')
plt.plot(merged_df['Year'], merged_df['Close_NVDA'], marker='o', linestyle='-', label='Nvidia (NVDA)')
plt.plot(merged_df['Year'], merged_df['Close_TSLA'], marker='o', linestyle='-', label='Tesla (TSLA)')

# Configurar el gráfico
plt.title('Evolución del Precio de Cierre de las Magnificent 7 (2014 - Presente)')
plt.xlabel('Año')
plt.ylabel('Precio de Cierre')
plt.legend()
plt.grid(True)
plt.show()



# Realizar el merge de los DataFrames anuales uno por uno utilizando la fecha como índice
merged_annual = apple_annual.join(amazon_annual, how='outer')
merged_annual = merged_annual.join(google_annual, how='outer')
merged_annual = merged_annual.join(meta_annual, how='outer')
merged_annual = merged_annual.join(microsoft_annual, how='outer')
merged_annual = merged_annual.join(nvidia_annual, how='outer')
merged_annual = merged_annual.join(tesla_annual, how='outer')



# Crear una tabla adicional que solo muestre las columnas 'High' y 'Low' para cada compañía utilizando los nombres correctos
high_low_annual = pd.DataFrame({
    'apple_high': apple_annual['High_AAPL'],
    'apple_low': apple_annual['Low_AAPL'],
    'amazon_high': amazon_annual['High_AMZN'],
    'amazon_low': amazon_annual['Low_AMZN'],
    'google_high': google_annual['High_GOOGL'],
    'google_low': google_annual['Low_GOOGL'],
    'meta_high': meta_annual['High_META'],
    'meta_low': meta_annual['Low_META'],
    'microsoft_high': microsoft_annual['High_MSFT'],
    'microsoft_low': microsoft_annual['Low_MSFT'],
    'nvidia_high': nvidia_annual['High_NVDA'],
    'nvidia_low': nvidia_annual['Low_NVDA'],
    'tesla_high': tesla_annual['High_TSLA'],
    'tesla_low': tesla_annual['Low_TSLA']
})


# Crear una nueva columna que calcule el porcentaje entre High y Low para cada compañía por año
high_low_annual['apple_percent_change'] = ((high_low_annual['apple_high'] - high_low_annual['apple_low']) / high_low_annual['apple_low']) * 100
high_low_annual['amazon_percent_change'] = ((high_low_annual['amazon_high'] - high_low_annual['amazon_low']) / high_low_annual['amazon_low']) * 100
high_low_annual['google_percent_change'] = ((high_low_annual['google_high'] - high_low_annual['google_low']) / high_low_annual['google_low']) * 100
high_low_annual['meta_percent_change'] = ((high_low_annual['meta_high'] - high_low_annual['meta_low']) / high_low_annual['meta_low']) * 100
high_low_annual['microsoft_percent_change'] = ((high_low_annual['microsoft_high'] - high_low_annual['microsoft_low']) / high_low_annual['microsoft_low']) * 100
high_low_annual['nvidia_percent_change'] = ((high_low_annual['nvidia_high'] - high_low_annual['nvidia_low']) / high_low_annual['nvidia_low']) * 100
high_low_annual['tesla_percent_change'] = ((high_low_annual['tesla_high'] - high_low_annual['tesla_low']) / high_low_annual['tesla_low']) * 100



# Filtrar la tabla 'high_low_annual' para mostrar solo los años de 2019 a 2021 y crear una nueva tabla llamada 'covid'
covid_table = high_low_annual.loc['2019':'2021']

# Mostrar la nueva tabla 'covid' que contiene los datos filtrados de 2019 a 2021
covid_table



# Aplicar una escala logarítmica para manejar mejor los valores extremos
log_heatmap_data = np.log1p(heatmap_data)  # Log(1 + x) para evitar problemas con ceros

# Crear el heatmap ajustado
plt.figure(figsize=(10, 6))

sns.heatmap(log_heatmap_data, cmap='coolwarm', annot=heatmap_data, fmt=".2f", linewidths=.5,
            cbar_kws={'label': 'Log de Porcentaje de Cambio (%)'})

plt.title('Heatmap de Volatilidad y Cambio Porcentual (Log) de las Magnificent 7 (2019-2021)')
plt.xlabel('Compañía')
plt.ylabel('Año')
plt.xticks(rotation=45)
plt.show()



# Filtrar los DataFrames mensuales para mostrar solo los años de 2021 a 2022 y hacer merge para graficar todas las compañías juntas
def filter_and_merge_monthly_data(df, company_name):
    df_filtered = df.loc['2021':'2022', ['Close']].copy()  # Filtrar solo los datos de 2021 a 2022
    df_filtered['Month'] = df_filtered.index  # Mantener el índice de meses
    df_filtered.columns = ['Close', 'Month']  # Renombrar las columnas
    df_filtered['Company'] = company_name  # Añadir la compañía
    return df_filtered

# Aplicar la función a cada compañía mensual
apple_monthly_filtered = filter_and_merge_monthly_data(apple_monthly, 'Apple')
amazon_monthly_filtered = filter_and_merge_monthly_data(amazon_monthly, 'Amazon')
google_monthly_filtered = filter_and_merge_monthly_data(google_monthly, 'Google')
meta_monthly_filtered = filter_and_merge_monthly_data(meta_monthly, 'Meta')
microsoft_monthly_filtered = filter_and_merge_monthly_data(microsoft_monthly, 'Microsoft')
nvidia_monthly_filtered = filter_and_merge_monthly_data(nvidia_monthly, 'Nvidia')
tesla_monthly_filtered = filter_and_merge_monthly_data(tesla_monthly, 'Tesla')

# Combinar todos los DataFrames filtrados en uno solo
merged_monthly = pd.concat([apple_monthly_filtered, amazon_monthly_filtered, google_monthly_filtered,
                            meta_monthly_filtered, microsoft_monthly_filtered, nvidia_monthly_filtered,
                            tesla_monthly_filtered])

# Graficar todas las compañías en un solo gráfico mensual
plt.figure(figsize=(12, 8))

# Graficar cada compañía
for company in merged_monthly['Company'].unique():
    company_data = merged_monthly[merged_monthly['Company'] == company]
    plt.plot(company_data['Month'], company_data['Close'], marker='o', linestyle='-', label=company)

# Configurar el gráfico
plt.title('Evolución Mensual del Precio de Cierre de las Magnificent 7 (2021-2022)')
plt.xlabel('Mes')
plt.ylabel('Precio de Cierre')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()



# Valores cercanos a 1: Indican que las compañías tienden a moverse juntas (positivamente correlacionadas).
# Valores cercanos a -1: Indican que las compañías tienden a moverse en direcciones opuestas (negativamente correlacionadas).
# Valores cercanos a 0: Indican poca o ninguna relación entre las compañías.

# Crear un nuevo DataFrame con los precios de cierre de cada compañía
closing_prices = covid_table[['apple_percent_change', 'amazon_percent_change', 'google_percent_change',
                              'meta_percent_change', 'microsoft_percent_change', 'nvidia_percent_change',
                              'tesla_percent_change']]

# Renombrar las columnas para que sean más claras
closing_prices.columns = ['Apple', 'Amazon', 'Google', 'Meta', 'Microsoft', 'Nvidia', 'Tesla']

# Calcular la matriz de correlación
correlation_matrix = closing_prices.corr()

# Crear el heatmap de correlación
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)

# Configurar el gráfico
plt.title('Matriz de Correlación de las Magnificent 7')
plt.show()


