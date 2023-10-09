"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = (pd.read_csv('solicitudes_credito.csv', sep=';')
          .drop(columns=['Unnamed: 0'], axis=1)
          .dropna())

    for column in df.columns:
        df[column] = (df[column].astype(str)
                      .str.lower()
                      .str.replace('-', ' ')
                      .str.replace('_', ' ')
                      .str.replace(',', '')
                      .str.replace('$', '')
                      )

    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)
    df.drop_duplicates(inplace=True)

    return df
