import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#Nota: Ya no se utiliza get_value ahora se utiliza at[valor] y iat[valor]
#idxmax devuelve el indice mayor 

"""
datos = pd.read_csv('Archivos_csv/movies2.csv')
df = pd.DataFrame(datos)
print("Maxima duracion de las peliculas")
print(df['duration'].max())
print()
print(df['duration'].max()/60)
print("La pelicula que dura mas es: ")
print(df['duration'].idxmax())
print(df.at[(df['duration'].idxmax(),'movie_title')])
print("Comparacion de like entre generos")
#      columna para agrupar datos    col selecionada del DataFrame
#                     |                  |
df1 = df.groupby(['genres'])[['movie_facebook_likes']].sum()# <- operacion sobre la columna
print(df1)
print()
print("Genero mas buscado en facebook")
likes = df.groupby(['genres'])[['movie_facebook_likes']].sum()
print(likes['movie_facebook_likes'].idxmax(),end="")
print("Con:", likes['movie_facebook_likes'].max(),"likes")
print()
print("Presupuesto promedio por director")
df2 = df.groupby(['director_name'])[['budget']].mean()
print(df2)
print("Genero que gatas mas dinero")
dinero = df.groupby(['genres'])[['budget']].sum()
print(dinero)
print()
print("Genero:",dinero['budget'].idxmax(),"con",dinero['budget'].max())
print()
print("Actor principal que atrae mas ganancias")
actor = df.groupby(['actor_1_name'])[['gross']].sum()
print(actor['gross'].idxmax(),"con", actor['gross'].max())
"""

#Extraer horas, minutos y segundos de columnas archivo csv CAP 11
"""
datos = pd.read_csv('Archivos_csv/datosnum.csv')

df = pd.DataFrame(datos)

hora = df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
print(hora)

df2 = pd.DataFrame(datos)
df2 = df2.fillna(0)

df2['A'] = df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')

df2['C'] = df['C'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')

df2['F'] = df['F'].str.extract('(\d+(?:\.\d+)?)')

df2['G'] = df['G'].str.extract('(\d+(?:\.\d+)?)')

print(df2)

print("Agrupaciones pos minuto")
print()
df2['A'] = pd.DatetimeIndex(df2['A'])
df2.set_index(keys='A', inplace=True)
inicio = datetime.time(11,18,0)
fin = datetime.time(11,19,0)
print(df2[['F']].between_time(inicio, fin))
"""

#Extraer números en columnas de un archivo csv CAP 11 part 2
"""
datos = pd.read_csv('Archivos_csv/datosnum.csv')
df = pd.DataFrame(datos)

#numero = df['F'].str.extract('(\d+(?:\.\d+)?)')
#print(numero)

df2 = pd.DataFrame()
df2 = df2.fillna(0)

for i in df.columns:

	df[i] = df[i].str.extract('(\d+(?:\.\d+)?)')

print("Iterando sobre todas la columnas")

print(df)
print()

print("Sin NaN")
df.fillna(0, inplace=True)
print(df)
"""

# CAP 12 Cómo restar tiempo| Extraer strings | Expresión regular

#datos = pd.read_csv('Archivos_csv/ArtJan2018resumido.csv')

#df = pd.DataFrame(datos)
#df['Date'] = df['pubDate'].str.extract('(../../..)', expand=True)#Extraer la fecha de una columna
#print(df['Date'])

"""
datos = pd.read_csv('Archivos_csv/Ejemplo.csv')
df = pd.DataFrame(datos)
df['Hora'] = df['fecha'].str.extract('(..:..:..)', expand=True)#Exraer horas de una columna
print(df['Hora'])
df['Hora'] = pd.to_datetime(df['Hora'])
df['hora 1'] = pd.to_datetime(df['hora 1'])
df['Resta Horas'] = df['Hora'] - df['hora 1']
print(df['Resta Horas']) 
print()
print(df)

plt.plot(df['Hora'], df['valor 2'], '-')
valor = plt.xticks(rotation=45)
print(valor)
"""
#Buscar un valor en una columna y extraer datos de otra CAP 12

datos = pd.read_csv('Archivos_csv/precios.csv')
df = pd.DataFrame(datos)
#print(df)

compra = "Piña cayene mediana"
piezas = np.random.randint(1, 20)
precio = df[df['producto'] == compra]['precio']

def total(piezas, precio):

	return precio*piezas

#print("El pago total a pagar:", total(piezas, precio))

#Agregar una columna a un Data Frame
"""
datos = pd.read_csv('Archivos_csv/minutos2.csv', header=0)
df = pd.DataFrame(datos)
print("Data Frame original")
print(df)

col = df['C']+237.8
df = df.assign(nueva=col.values)
#df.insert(4, 'nueva', col)
print("Data Frame modificado")
print(df)
df.to_csv('min_modif.csv', sep='\t')
"""

datos = pd.read_csv('Archivos_csv/student-mat.csv')
df = pd.DataFrame(datos)
df1 =datos.loc[(df['school'] == 'GP')]
df2 = datos.loc[(df['school'] == 'MS')]
"""

#print(df.infer_objects().dtypes)
print()

print(df2.info())
print()
print("Estudiantes que viajan mas de una hora")
print(df1.where(df1.traveltime == 4).traveltime.count())
print()
print("Estadisticas básicas")
print(df1['traveltime'].describe())
plt.figure
df1['traveltime'].hist()
"""
print("Estudiantes sin internet")
print(df1.where(df1.internet == 'no').internet.count())
print()
print("Relaciones familiares de los estudiantes")
print()
print(df1.where(df.famrel == 1).famrel.count())
print()
tabla = pd.pivot_table(df1, index=['sex', 'Mjob'], values='famrel')
print(tabla)

print("Tabla pivote usuario")
"""
agrupar = input("Como quieres agruparlos datos?: ")
datos = input("Cual dato quieres analizar: ")

tabla1 = pd.pivot_table(df1, index=[agrupar], values=datos, aggfunc=[np.mean, min, max])
print(tabla1)
"""
if df1.where(df.famrel <= 2).famrel.count() > 0:
	print("Se requiere atencion especialzada")
	tutores = df1.where(df.famrel <=2).famrel.count()/2
	print("Se requiere", int(round(tutores,2)), "tutores")

