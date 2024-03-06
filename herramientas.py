import pandas as pd 
import geopandas as gpd

def verificar_tipo_datos(df): #verifica los nulos y no nulos
    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": []}
    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
    df_info = pd.DataFrame(mi_dict)
    for columna in df.columns:
        print(columna, " (nulos) = ", df[columna].isnull().sum())
    print("\nfilas completamente nulas: ", df.isna().all(axis=1).sum())

    return df_info

def verificar_datos_unicos(df): #determina si estan repetidos 
    columnas_df = df.columns.tolist()
    tipos_datos = [float, int, str]
    for columna in columnas_df:
        for tipo in tipos_datos:
            filtro = df[columna][df[columna].apply(lambda x: isinstance(x, tipo))]
            valores_unicos = filtro.unique()
            print(columna, " (", tipo.__name__, ") ", len(valores_unicos),": ", valores_unicos)
        print("")

def determinar_semestre(mes): #se crea una columna para determinar una variable por SEMESTRE
    if mes <= 6:
        return 1
    else:
        return 2
#Ej:df["Semestre"] = df["MM"].apply(determinar_semestre)
#   df.groupby(["AAAA", "Semestre"])["N_VICTIMAS"].sum().reset_index()

def convert_to_geometry(coord): #ayuda a convertir las coordenadas recibidas en un formato que geopandas pueda leer
    try:
        geometry = loads(coord)
        return geometry
    except Exception as e:
        return None