# Proyecto ETL en Python

Este proyecto consta de un script en Python que realiza procesos de Extracción, Transformación y Carga (ETL) para dos conjuntos de datos: `mibici_12-2014_01-2024.csv` y `nomenclatura_2024.csv`.

## Descripción del Proyecto

El objetivo de este proyecto es crear un script en Python utilizando `__main__` para ejecutar dos ETLs diferentes, cada uno con su propio archivo CSV de entrada y salida.

## Características del Proyecto

1. Un script principal para ejecutar todas las ETLs.
2. Más de un ETL para datasets distintos.
3. Creación de una columna con la fecha y hora de extracción en ambos ETLs.
4. Reutilización de funciones para mejorar la eficiencia y la legibilidad del código.
5. Implementación de buenas prácticas de Python según el Manifesto y PEP8.

## Estructura del Proyecto

- `main.py`: Script principal para ejecutar los ETLs.
- `class_etl.py`: Clase `ETL_Handler` para gestionar el proceso ETL.
- `class_extraction.py`: Clase `Extraction` para la extracción de datos.
- `class_transform.py`: Clase `Transform` para la transformación de datos.
- `class_load.py`: Clase `Load` para la carga de datos.
- `/files`: Directorio que contiene los archivos CSV de entrada y salida.

## Uso del Script

Para ejecutar el script y realizar un ETL específico, sigue los siguientes pasos:

1. Abre una terminal o línea de comandos.
2. Navega al directorio del proyecto.
3. Ejecuta el siguiente comando para obtener ayuda e información de uso:

```bash
python main.py --help
```
4. **Si no proporcionas un argumento -etl, el script ejecutará automáticamente ambos ETLs.**

## Fuente para descargar los archivos de prueba

Los archivos de prueba utilizados en este proyecto pueden ser descargados desde la siguiente fuente:

- **Mibici - Uso de Bicicletas Públicas de 2014 al 2024**
  - **URL:** [Kaggle - Mibici Dataset](https://www.kaggle.com/datasets/sebastianquirarte/mibici-uso-de-bicicletas-pblicas-de-2014-al-2024)
  - **Descripción:** Este dataset incluye datos del uso del servicio de bicicletas compartidas MiBici dentro de la zona metropolitana de Guadalajara (ZMG), Jalisco, México, desde diciembre 2014 hasta enero 2024 (incluye datos de 110 meses en total)..
