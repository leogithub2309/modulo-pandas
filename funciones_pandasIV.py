from pandas import read_excel
from IPython.display import display
import seaborn as sns
from datetime import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import zipfile
"""
df = pd.read_csv('Archivo_csv/VGMod.csv')
print(df.head(4))
colors  = ("dodgerblue","salmon", "palevioletred", 
           "steelblue", "seagreen", "plum", 
           "blue", "indigo", "beige", "yellow")

i = 0

for e in df[1:]:

	nin_wii = df[e].value_counts()
	
	graf = df[e].value_counts().plot(kind='pie', colors=colors, shadow=True, autopct='%1.1f%%',
									 startangle=30, radius=1.5, center=(0.5,0.5), textprops={'fontsize':12},
									 frame=False, labels=None ,pctdistance=.65)
	
	graf = df[e].value_counts().plot(kind='bar', colors=colors)
	labels = nin_wii.index.unique()
	plt.gca().axis('equal')
	plt.title(df.columns[i], weight='bold', size=14)
	plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
	plt.savefig(str(df.columns[i])+".png", dpi=100, bbox_inches="tight")
	graf.set_ylabel("")
	plt.legend(labels, bbox_anchor=(0.5, -.2))
	i += 1
	plt.show()
"""
"""
datos = pd.read_csv('Archivo_csv/data.csv')

colors  = ("dodgerblue","salmon", "palevioletred", 
           "steelblue", "seagreen", "plum", 
           "blue", "indigo", "beige", "yellow")

font = {
	
	'family': 'serif',
	'color': 'darkred',
	'weight': 'normal',
	'size': 16,
}

#print("Argentina:",str((datos.Nationality=='Argentina').sum()))

lista_paises = ['Bolivia', 'Colombia','Peru','Chile','Dominican Republic',
				'Mexico']

abreviatura = {
	
	'Bolivia': 'BOL',
	'Colombia': 'COL',
	'Peru': 'PE',
	'Chile': 'CL',
	'Dominican Republic': 'DO',
	'Mexico': 'MX',
}

datos = datos.set_index(['Nationality'])

dicc = {
	
	'cols': ['Club','Preferred Foot',
			 'International Reputation','Work Rate', 'Body Type']
}

j = 0
zf = zipfile.ZipFile('data.zip', mode='w')

for y in lista_paises:
	df1 = datos.loc[lista_paises[j]]
	df1[dicc['cols']]
	i = 0
	for e in df1:
		nin_wii = df1[e].value_counts()
	
		graf = df1[e].value_counts().plot(kind='pie', colors=colors, shadow=True, autopct='%1.1f%%',
									 startangle=30, radius=1.5, center=(0.5,0.5), textprops={'fontsize':12},
									 frame=False, labels=None ,pctdistance=.65)
	
		labels = nin_wii.index.unique()
		plt.gca().axis('equal')
		plt.title(df1.columns[i], weight='bold', size=14)
		plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
		graf.set_ylabel("")
		plt.legend(labels, bbox_to_anchor=(0.5, -.2))

		plt.savefig(str(abreviatura[lista_paises[j]])+str(df1.columns[i])+".png", dpi=100, bbox_inches="tight")
		zf.write(str(abreviatura[lista_paises[j]])+str(df1.columns[i])+".png")
		plt.show()
		i += 1
	j += 1
zf.close()

"""
df = sns.load_dataset('tips')
print(f"{df.shape[0]} Filas y {df.shape[1]} Columnas")
print()
print(df.head(10))
print()
print(df.query("tip > 6 & total_bill >= 30"))
media = df['tip'].median()
print(df.query("tip > @media").head())
print()
df.rename(columns={'total_bill':'totals_bill'}, inplace=True)
print(df.query("totals_bill < 20").head())
df.rename(columns={'totals_bill': 'total_bill'}, inplace=True)
print()
print(df.query("total_bill > 20").head())
print()
display(df.head())
print()
print(df.tail())
print()
display(df.query("day == 'Sat'").head())
print()
display(df.query('day == "Sat"').head(10))
print()
df['rev_tip'] = -df['tip']
print(df.sort_values(by=['total_bill', 'rev_tip'], ascending=True).head())
del df['rev_tip']
print()
print(df.sort_values(by=['total_bill', 'tip'], ascending=[True, False]).head())
print()
print(df.nsmallest(5, 'total_bill'))
print(df.sort_values(by='total_bill').head())
print()
display(df.nlargest(5, 'total_bill'))
print()
print(df.sort_values(by='total_bill', ascending=False).head())
print()
display(df.describe(include=['category']))
display(df.describe(include=['number']))
print()
print(f" {pd.options.display.max_columns} columns")
print(f"{pd.options.display.max_rows} rows")
pd.options.display.max_columns = 100
pd.options.display.max_rows = 50
pd.options.display.float_format = '{:.4f}'.format
print(pd.options.display.float_format)