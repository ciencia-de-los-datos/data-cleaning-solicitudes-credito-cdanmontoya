"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = (pd.read_csv('solicitudes_credito.csv', sep=';')
          .dropna()
          .drop_duplicates(ignore_index=True))

    for column in df.columns:
        df[column] = (df[column].astype(str)
                      .str.lower()
                      .str.replace('-', ' ')
                      .str.replace('_', ' ')
                      .str.replace(',', '')
                      .str.replace('$', '')
                      .str.strip())

    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)

    return df
