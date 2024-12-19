import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calcular_porcentajes(df, columnas):
    """
    Calcula los porcentajes para las columnas especificadas en un DataFrame.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        columnas (list): Lista de nombres de columnas para calcular el porcentaje.

    Returns:
        pd.DataFrame: DataFrame actualizado con las columnas de porcentaje.
    """
    for columna in columnas:
        total = df[columna].sum()
        if total > 0:
            nueva_columna = f'Porcentaje_{columna}'
            df[nueva_columna] = (df[columna] / total) * 100
        else:
            print(f"El total de la columna {columna} es 0. No se calcularán porcentajes.")
    return df



def lineplot_datos_agrupados(df,list_columns):
    """
   
    """
    
    for column in list_columns:
        plt.plot(df.index, df[column], marker='o', label=column)

    # Anadir título, leyenda y etiquetas
    plt.title('Valores Categoría Económica', fontsize=16)
    plt.xlabel('Categoría Económica', fontsize=14)
    plt.ylabel('Valor', fontsize=14)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, fontsize=12)
    plt.grid(True)

        # Mostrar el grafico
    return plt.show()



def barplot_descriptive(df,columns_list):

#columnas_interes = ['valor_previsto_actualizado', 'valor_lanzado', 'valor_realizado', 'percentual_realizado', 'diferencia_realizado_previsto'] 
#columnas_interes = ['valor_previsto_actualizado', 'valor_lanzado', 'valor_realizado', 'diferencia_realizado_previsto'] 
#columnas_interes = ['valor_previsto_actualizado', 'valor_realizado'] 
    descriptivos = []

    for col in columns_list:
    
        # Calculo el rango que pandas no lo hace con el descriptve
        min_val = df[col].min()
        max_val = df[col].max()
        mean_val = df[col].mean()
        std_val = df[col].std()
        range_val = max_val - min_val #https://bilalmussa.medium.com/calculating-mathematical-range-in-python-for-pandas-describe-50898bae7405
        
        # pongo los resultados en la lista, donde cada estadistico es una clave de un diccionario para cada columna
        descriptivos.append({
            'columna': col,
            'min': min_val,
            'max': max_val,
            'mean': mean_val,
            'std': std_val,
            'range': range_val
        })
    print(descriptivos)
    # Convertir la lista de resultados a un DataFrame
    df_descriptivo_rangos = pd.DataFrame(descriptivos)

    # Mostrar el DataFrame con los resultados
    print(df_descriptivo_rangos)

    # Visualización con seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_descriptivo_rangos.melt(id_vars=['columna'], var_name='métrica', value_name='valor'), ## https://www.geeksforgeeks.org/python-pandas-melt/
                x='columna', y='valor', hue='métrica')
    plt.title('Estadísticas descriptivas por columna')
    plt.xticks(rotation=45)
    plt.ylabel('Valor')
    plt.xlabel('Columna')
    plt.legend(title='Métrica')
    plt.tight_layout()
    plt.show()



