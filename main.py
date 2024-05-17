import argparse
from class_etl import ETL_Handler
from class_extraction import Extraction
from class_transform import Transform
from class_load import Load

def run_etl_mibici():
    # Una clase para ambos ETLs

    etl_mibici = ETL_Handler("files/mibici_12-2014_01-2024.csv", "latin1")
    df_mibici = etl_mibici.extract_info()
    df_mibici = etl_mibici.transform(df_mibici)
    etl_mibici.load(df_mibici, 'mibici_extracted.csv')

    # Una Clase para cada etapa del etl:

    extraction = Extraction("files/mibici_12-2014_01-2024.csv", "latin1")
    df_mibici = extraction.extract_info()

    transform = Transform(df_mibici)
    df_mibici_transformed = transform.transform_df()

    load = Load(df_mibici_transformed, "mibici_extracted.csv")
    load.load_file()

def run_etl_nomenclatura():
    # Una clase para ambos ETLs

    etl_nomenclatura = ETL_Handler("files/nomenclatura_2024.csv", "latin1")
    etl_nomenclatura.result_csv()

    # Una Clase para cada etapa del etl:

    extraction = Extraction("files/nomenclatura_2024.csv", "latin1")
    df_nom = extraction.extract_info()

    transform = Transform(df_nom)
    df_nom_transformed = transform.transform_df()

    load = Load(df_nom_transformed, "nom_extracted.csv")
    load.load_file()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script principal para ejecutar diferentes ETLs. Se puede elejir qué ETL ejecutar. Opciones: mibici/nomenclatura')
    parser.add_argument('-etl', type=str, choices=['mibici', 'nomenclatura' ], required=False, help='Indica qué ETL ejecutará')

    args = parser.parse_args()

    if args.etl == 'mibici':
        run_etl_mibici()
    elif args.etl == 'nomenclatura':
        run_etl_nomenclatura()
    else:
        print("El script se está ejecutando desde el editor de código.")
        print("Ejecutando ambos ETLs...")

        run_etl_mibici()
        run_etl_nomenclatura()




