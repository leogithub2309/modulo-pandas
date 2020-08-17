import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from validate_email import validate_email
from pandas import read_excel
"""
df = pd.read_csv('Archivos_csv/student-mat.csv')
#df = pd.DataFrame(datos)
df['health'].fillna(0, inplace=True)

df1 = df.loc[(df['school'] == 'MS')]
df2 = df.loc[(df['school'] == 'GP')]

faltas = len(df1[(df1['absences'] > 10) & (df1['failures'] < 2)])
print(faltas)

print("*"*20)
print()
print(df1.loc[(df1['absences'] > 10) & (df1['failures'] < 2),('health', 'sex', 'traveltime')])
print()
fallas = df1[(df1['absences'] > 10) & (df1['failures'] < 2)].count()['absences']
print(fallas)

print("*"*20)
print(df1[df1['age'] > 20]['sex'])#informacion con valor y posicion

print("*"*20)
print(df1[df1['age'] > 20].iloc[0]['sex'])#informacion solo con el valor

print("Relacion entre el consumo de alcohol y el tiempo libre")
print()
print(df1['freetime'].corr(df1['Dalc']))
print(df1['Dalc'].corr(df1['famrel']))

dicc = {'Muy bajo':1, 'Bajo':2, 'Medio':3, 'Alto':4, 'Muy Alto':5}

df1.Dalc.value_counts().plot(kind='pie', labels=None, autopct='1.2F%%', shadow=True,
							 startangle=180, fontsize=12, pctdistance=1.2, labeldistance=1.4)

plt.title("Consumo de Alcohol")
plt.legend(loc="best", labels=dicc)
plt.ylabel('H')
plt.axis('equal')
plt.show()

import seaborn as sns

sns.set(style="ticks", color_codes=True)
nuevo = df[['G1', 'G2', 'G3']].copy()
grap = sns.pairplot(nuevo, kind='reg')
"""

"""
lista_xls = []

for f in glob.glob("*.xlsx"):
	df = pd.read_excel(f)
	lista_xls.append(pd.read_excel(f))

df = pd.concat(lista_xls, ignore_index='True')
#print(df)

#df = df.replace(0, np.nan).ffill()

writer = pd.ExcelWriter('Ordenes.xlsx')
df.to_excel(writer, 'Hoja 1')
writer.save()

datos_xls = pd.ExcelFile(nombre)
hoja = datos_xls.parse('Orders')
df = pd.DataFrame(hoja)
writer = pd.ExcelWriter('Ordenes.xlsx')
df.to_excel(writer, 'Hoja 1')
writer.save()


xls = pd.ExcelFile('Archivos_csv/sales2.xls')

hojas = []

for hoja in xls.sheet_names:
	df = xls.parse(hoja)
	hojas.append(df)


estado = pd.concat(hojas, ignore_index=True)
print(estado.shape)

guardar = pd.ExcelWriter('Todo.xlsx')
estado.to_excel(guardar, 'Hojas')
guardar.save()

df = pd.read_csv('Archivos_csv/datoscorreos - Sheet1.csv')
print(df.head(5))
print()
print(len(df['correos']))

df['verificar'] = df['correos'].apply(lambda n: validate_email(n))
df['error'] = ""
df['ok'] = ""

df['error'].mask(df['verificar'] == False, df.correos, inplace=True)
df['ok'].mask(df['verificar'] == True, df.correos, inplace=True)
#df['error'] = np.where(df['is_valid_email'] == False, df.correos, df['error']])

df['error'] = df['error'].sort_values(ascending=False).values
df['ok'] = df['ok'].sort_values(ascending=False).values


df.to_csv('ValidacionEmail.csv', header=True, index=False)
"""

archivo = 'Archivos_csv/pruebaxls.xlsx'
hoja = '17'
xls = read_excel(archivo, sheet_name=hoja)

print(xls['channel_title'].nunique())
print(xls['channel_title'].count())

datos = pd.DataFrame()
dicc = pd.read_excel(archivo, sheet_name=None)

for name,col in dicc.items():

	col['title'] = name
	datos = datos.append(col, ignore_index=True)

	print(name)
"""
datos['completos'] = datos['year']
print(datos['completos'].head(4))
datos['completos'] = datos['completos'].map({'14':2014, '15':2015, '16':2016, '17':2017})
print()
print(datos['completos'].head(4))
print(datos['channel_title'].count())
print()
print(datos['channel_title'].unique())

#datos.transpose()
datos.to_csv('CanalesYoutube.csv')
"""