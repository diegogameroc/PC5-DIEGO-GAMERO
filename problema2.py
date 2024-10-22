"""
Lea el archivo 'winemag-data-130k-v2.csv' y realice lo siguiente:

- Explore el dataframe según lo visto en clase
- Realice al menos  4 renombre de columna y 3 creación de nuevas columnas según criterio. Deberá crear las columnas que crea conveniente. 
    Ejemplo: Según el país etiquetelos según continente.

- Genere 4 reportes distintos(podria agrupando, filtrar, ordenar, etc). Deberá elegir que reportes realizar
    - Ejemplo: Por contienente mostrar los vinos mejor puntuados
    - Ejemplo2: Promedio de precio de vino y cantidad de reviews obtenidos según pais. Ordenado de mejor a peor.



- Exporte los 4 reportes a 4 formatos de archivos diversos, csv, excel, sqllite, mongodb...
   
   Para guardar datos de datos agrupados, puede revisar esta solución https://stackoverflow.com/questions/25789264/pandas-dataframegroupby-export-to-excel

- Envie uno de los reportes generados por correo, mostrar un pantallazo del correo enviado

"""

import pandas as pd

df = pd.read_csv('/workspaces/PC5-DIEGO-GAMERO/data/winemag-data-130k-v2.csv')
df.head()




