import pandas as pd

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