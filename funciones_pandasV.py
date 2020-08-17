from pandas import read_excel
from IPython.display import display
from datetime import *
from textblob import TextBlob
from fuzzywuzzy import process

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import zipfile
"""
datos = pd.read_csv('Archivo_csv/GBvideos.csv')
df = pd.DataFrame(datos)

#ax = sns.distplot(df['views'])
lista = ['views', 'likes', 'dislikes', 'comment_count']
#sns.pairplot(df, vars=lista, hue='category_id', palette='Paired')

vistas = (df['views'] > 1e6)&(df['views'] < 10e6)
nuevo = df[vistas]
print(df.loc[df['category_id'] == 22]['views'].sum())

etiquetas = {

    2: 'Autos & Vehicles',1:'Film & Animation',10:'Music',
    15 : 'Pets & Animals',17 : 'Sports',18 : 'Short Movies',
    19 : 'Travel & Events',20 : 'Gaming',21: 'Videoblogging',
    22 : 'People & Blogs',23:'Comedy',24:'Entertainment',
    25 : 'News & Politics',26 : 'Howto & Style',27 : 'Education',
    28 : 'Science & Technology',29 :'Nonprofits & Activism',
    30 : 'Movies',31 : 'Anime/Animation',32 : 'Action/Adventure',
    33 : 'Classics',34 : 'Comedy',35 : 'Documentary',36 : 'Drama',
    37 : 'Family',38 : 'Foreign',39 : 'Horror',40 : 'Sci:Fi/Fantasy',
    41 : 'Thriller',42 : 'Shorts',43 : 'Shows',44 : 'Trailers'

}
print(df['category_id'].head(5))
print()
df['category_id_n'] = df['category_id']
df['category_id_n'] = df.category_id_n.map(etiquetas)
print(df['category_id_n'].head(5))
print()
print(df.head(5))
print()
grupo = df.groupby('category_id_n').views.sum().reset_index().sort_values('views', ascending=False)
print(grupo)

var = sns.pairplot(df, x_vars=['likes', 'dislikes'],
				   y_vars=['views', 'comment_count'], hue='category_id', palette='Paired')

datos = pd.read_csv('Archivo_csv/nyt.csv')

#datos['traduccion'] = datos['content'].apply(lambda n: Textblob(n).translate(to='es'))
#print(datos['traduccion'].head(10))

datos['traduccion'] = datos['content'].apply(lambda n: TextBlob(n).sentiment.polarity)

datos['subobj'] = datos['content'].apply(lambda n: TextBlob(n).sentiment.subjectivity)

#sns.displot(df['traduccion'])
#sns.distplot(df['subobj'])

n = 0

while n < 5:

	datos['P'+str(n)] =  datos['content'].apply(lambda n: TextBlob(n).sentiment.polarity)

	datos['S'+str(n)] = datos['content'].apply(lambda n: TextBlob(n).sentiment.subjectivity)

	n += 1
"""
"""
datos = pd.read_csv('Archivo_csv/googleplaystore - googleplaystore.csv')

tabla = pd.pivot_table(datos, index=['Content Rating','Category'],values=['Rating'],
					   columns=['Type'], aggfunc='count')
#print(tabla)
writer = pd.ExcelWriter('pivot.xlsx')
tabla.to_excel(writer, 'GoogleApp')
writer.save()

datos = pd.read_csv('Archivo_csv/fomix - fomix.csv')
#print(list(datos))
print(datos.head(20))
tabla = pd.pivot_table(datos, index=['NOMBRE DEL SUJETO DE APOYO'], values=['MONTO'],
					   columns=['FOMIX'], aggfunc='sum')
values--> valores de la tabla, index--> clasificacion de la tabla,
columns --> depende de los valores de la columna					


lectura = pd.ExcelWriter('pivot.xlsx')
tabla.to_excel(lectura, 'Fomix')
lectura.save()

datos = pd.read_csv('Archivo_csv/Becas2017 - becas.csv')
print(list(datos))
tabla = pd.pivot_table(datos, index=['Nivel','Género'], values=['Institución'],
					   columns=['País Destino'], aggfunc='count')

lectura = pd.ExcelWriter('pivot.xlsx')
tabla.to_excel(lectura, 'Becas')
lectura.save()
"""
"""
dicc = pd.read_csv('Datos.csv', header=None, index_col=0, squeeze=True).to_dict()

df = pd.read_csv('Archivo_csv/precioOro.csv')
print(df.info())
df['abreviatura'] = df['Estados'].map(dicc).fillna('*',inplace=True)
df['Estados'] = df['Estados'].str.strip()
dicc['Gurero'] = 'GRO'

df['Estados'].replace('Gurero','Guerrero',inplace=True)
df['Estados'] = df['Estados'].replace('Gurero','Guerrero')
"""
ok = {'México','Venezuela','Ecuador','Brazil'}#python-Levenshtein
dato = "venezula"
aprox = process.extractOne(dato, ok)
#print(aprox)
print()
df = pd.read_csv('Archivo_csv/wuzy.csv')
print(df)

nombres = []
proporcion = []

def coincidencias(mal,bien):

	for i in mal:
		valor = process.extractOne(i, bien)
		nombres.append(valor[0])
		proporcion.append(valor[1])
	return nombres,proporcion

mal = df['mal'].dropna().values
bien = df['bien'].dropna().values

corregido, rango = coincidencias(mal, bien)
df['Corregido'] = pd.Series(corregido)
df['Rango'] = pd.Series(rango)

print(df)