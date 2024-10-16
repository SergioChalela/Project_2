import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Función para cargar los datasets
def load_datasets():
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
    
    return apple, amazon, google, meta, microsoft, nvidia, tesla

# Función para convertir la columna 'Date' a formato datetime
def convert_dates(dataframes_dict):
    for name, df in dataframes_dict.items():
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return dataframes_dict

# Función para crear DataFrames filtrados (solo 'Date', 'Open', 'High', 'Low', 'Close')
def filter_dataframes(dataframes_dict):
    return {name: df[['Date', 'Open', 'High', 'Low', 'Close']] for name, df in dataframes_dict.items()}

# Función para resumir por mes y año
def resample_dataframes(filtered_dataframes, freq):
    return {name: df.resample(freq, on='Date').mean() for name, df in filtered_dataframes.items()}

# Función para crear DataFrames de gráficos (Close por año)
def create_grafico_general(df, close_column, company_name):
    company_grafico_general = df[[close_column]].copy()
    company_grafico_general['Year'] = company_grafico_general.index.year
    company_grafico_general = company_grafico_general[['Year', close_column]]
    company_grafico_general.columns = ['Year', f'Close_{company_name}']
    return company_grafico_general

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

# Función para combinar varios DataFrames en uno
def merge_dataframes(dataframes, on_column='Year'):
    merged_df = dataframes[0]
    for df in dataframes[1:]:
        merged_df = merged_df.merge(df, on=on_column)
    return merged_df



