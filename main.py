# Crear un script en python usando __main__ para extraer datos de dos archivos (mibici_12-2014_01-2024.csv,nomenclatura_2024.csv), cada uno con su etl y crear un archivo .csv para cada uno
# * Un script principal para ejecutar todas las ETLs
# * Debe ser creado más de un ETL para datasets distintos, (ej. extraer datos de dos apis y crear dos archivos)
# * Crear una columna con a fecha y hora de extraccion en los dos ETLs.
# * Intentar reutilizar funciones
# * Buscar cual la mejor manera de desarollar cada etapa (ETL) las opciones : crear una clase por etapa, o una clase por ETL.
# * Buenas Praticas de Python (Manifesto y PEP8)


# Un script principal para ejecutar los dos ETL.
# Probá una clase por etapa del ETL.
# Reutilizar funcciones
# Usar git o el drive para enviarme la solucción

from class_etl import ETL_Handler
from class_extraction import Extraction
from class_transform import Transform
from class_load import Load

if __name__ == "__main__":

    # Una clase para ambos ETLs
    ## Use dos maneras distintas para cada ETL

    etl_mibici = ETL_Handler("files/mibici_12-2014_01-2024.csv", "latin1")
    df_mibici = etl_mibici.extract_info()
    df_mibici = etl_mibici.transform(df_mibici)
    etl_mibici.load(df_mibici, 'mibici_extracted.csv')

    etl_nomenclatura = ETL_Handler("files/nomenclatura_2024.csv", "latin1")
    etl_nomenclatura.result_csv()

    # Una Clase para cada etapa del etl:

    extraction = Extraction("files/mibici_12-2014_01-2024.csv", "latin1")
    df_mibici = extraction.extract_info()

    transform = Transform(df_mibici)
    df_mibici_transformed = transform.transform_df()

    load = Load(df_mibici_transformed, "mibici_extracted.csv")
    load.load_file()

    extraction = Extraction("files/nomenclatura_2024.csv", "latin1")
    df_nom = extraction.extract_info()

    transform = Transform(df_nom)
    df_nom_transformed = transform.transform_df()

    load = Load(df_nom_transformed, "nom_extracted.csv")
    load.load_file()
