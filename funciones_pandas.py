import pandas as pd
import numpy as np
"""
def leer_archivo():
	archivo_csv = pd.read_csv("ATP.csv")#Cap 2 Leer la informacion de un arhivo .csv
	#print(archivo_csv.info())
	print()
	print(archivo_csv.head())
	print()
	datos = pd.DataFrame(archivo_csv)
	print(datos)
	datos = datos.replace(np.nan,'0')# Cambiando los valores de NaN por 0
	print(datos.info())
	print("\n"*2)
	print("Impresion de datos sin NaN")
	print(datos.describe(include=[np.number]))#Mostrando la estadisticas
	print("\n"*2)
	datos = datos.replace('N/A', '0')
	datos = datos.replace('NR','0')
	print("Estadisticas sin N/A")
	print(datos.describe())
	print(list(datos))
	print("\n"*2)
	datos['Wsets'] = datos.Wsets.astype(int)
	datos['WRank'] = datos.WRank.astype(int)
	print("\n"*2)
	print("******Estadisticas de los Wsets y WRank******")
	print(datos['Wsets'].describe())
	print("\n"*2)
	print(datos['WRank'].describe())
	print(""\n*1)
	archivo_csv.dropna(how='any', inplace=True)
	print(archivo_csv.head())
"""

#Seleccionar renglones y columnas de un archivo CSV
"""
archivo = pd.read_csv('ATP.csv')

print(archivo.head())
print("\n"*2)
print(archivo.iloc[0:5])#Muestra las primeras cinco columnas
print("\n"*2)
print(archivo.iloc[[2,5,7,46],])#Muestra las filas salteadas
#muestra por columnas
print("\n"*2)
print(archivo.iloc[:,0:5])
print(archivo.iloc[[2,5,7,46],[5,6,10]])
print(archivo.iloc[0:5,5:8])
"""
#Selección de renglones y columnas por nombre LOC CAP 3
"""
archivo = pd.read_csv("ATP.csv")

print(archivo.head())

archivo.set_index("Location", inplace=True)
print(archivo.loc['Melbourne'])
print()
print()
print(archivo.loc['Atlanta','Surface'])
print("Seleccion Amplia")
print(archivo.loc[['Atlanta','Melbourne'],['Series', 'Court']])
print()
print("Seleccion con rango")
print(archivo.loc[['Atlanta','Melbourne'], 'Series':'Round'])
print("Seleccion solamente de Gram Slam")
print(archivo.loc[archivo['Series'].str.endswith('Slam')])
"""

#Exportar a csv informacion mediante pandas en python
"""
datos = pd.read_csv("ATP.csv")
df = pd.DataFrame(datos)
df.reset_index().to_csv('DatosATP.csv', header=True, index=False)
datos.set_index("Location", inplace=True)
#Seleccionando datos por localizacion
df = datos.loc['Melbourne']
df.reset_index().to_csv('MelbourneATP.csv', header=True, index=False)
"""

#Cap 4 Búsqueda de datos con condiciones
"""
archivo = pd.read_csv("ATP.csv")
archivo.set_index("Location", inplace=True)
print(archivo.loc[archivo['Court'] == 'Outdoor', ['Surface', 'Winner']])
print()
print("Realizar busqueda con mas de una condicion")
print(archivo.loc[archivo['Series'].str.endswith('Slam') & (archivo['Surface'] == 'Clay') &
	(archivo['Winner']=='Federer R.')&(archivo['Round']=='The Final')])
"""
#Ordenar archivos por columnas Cap 5

"""
datos =  pd.read_csv('DatosYT.csv')

print(datos.dtypes)
print()
print(datos.sort_values(by=['id'],ascending=[True]))#Ordena dependiendo del argumento que se le pase a by
print()
df = pd.DataFrame(np.sort(datos.values, axis=0), index=datos.index, columns=datos.columns)
print(df)#Ordena todas las columnas

fichero = open('Datos.txt', 'w')

fichero.write(str(df))#df.to_string

fichero.close()
"""
#Borrar renglones de un archivo csv Cap 6
"""
datos = pd.read_csv('canciones.csv')
print(datos)
print()
print()
filas = len(datos.index)#Longiud de las filas del archivo csv
print("Filas:",filas)
print()
datos.drop(datos.index[10], inplace=True)
filas = len(datos.index)
print(filas)
print(datos)
"""
#Escribir información a un archivo csv Cap 7
"""
dicc = {
	
	'Sonora':'Hermosillo',
	'Nayarit': 'Tepic',
}

archivo = "estados.csv"

fichero = open(archivo, 'w')

titulo = "estado, capital\n"

fichero.write(titulo)

for key in dicc.keys():
	estado = key
	capital = dicc[key]
	filas = estado+","+capital+"\n"
	fichero.write(filas)

fichero.close()
"""
#CAP 8 Lectura archivo xls
"""
archivo_xls = pd.ExcelFile('sales2.xls')

print(archivo_xls.sheet_names)

df = archivo_xls.parse('Users')
print(df)
"""

#CAP 9 Operaciones con condición en columnas

minutos= pd.read_csv('Archivos_csv/minutos2.csv')

df = pd.DataFrame(minutos)
alto = df.loc[0,'B']

df['PB'] = df['B'].diff(1)

for i in range(1, len(df)):#Revisa el total de registros y los recorre uno a uno
	if df.loc[i,'B'] > df.loc[i-1,'B'] and df.loc[i, 'B'] > alto:
		df.loc[i,'dB'] = df.loc[i, 'B'] - alto # df.loc[i, 'dB'] =  se crea una nueva columna
		alto = df.loc[i, 'B']
	else:
		df.loc[i, 'dB'] = 0

print(df)
total = df['dB'].sum()
print(total)
print("Suma parcial  PB",df.loc[df['PB'] > 0, 'PB'].sum())
print()
print()
#df.reset_index().to_csv('Archivos_csv/', header=True, index=False)