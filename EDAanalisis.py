import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("USA_Housing.csv")#Leemos el archivo csv
data.head()#sacamos las primeras 5 filas de datos
data.columns#Vemos cuáles son las columnas de nuestro archivo

data.isnull().sum()#Usamos un método para ver si hay datos nulos y que devuelva la suma de todos los datos nulos que encuentre
data.duplicated().sum()#Usamos un método para ver si hay datos duplicados y que devuelva la suma de todos los datos duplicados que encuentre
data.info()#Vemos qué tipo de datos hay en el dataset
data.describe()#Sacamos los datos estadísticos del dataset

data.hist()#Histograma del dataset
data.hist("Area Population")#Histograma de la columna "Area Population"

data.plot()#Plot del dataset
plt.show()#Enseñamos el plot

sns.heatmap(data.corr(), annot=True)#Mapa de calor del dataset
plt.show()#Enseñamos el gráfico

sns.pairplot(data)#Pairplot del dataset
plt.show()#Enseñamos el pairplot

sns.boxplot(data=data, x='Avg. Area Income', y='Area Population')#Diagrama de cajas
plt.show()#Enseñamos el diagrama

for column in data:#Bucle que enseña los histplots de cada columna
        sns.histplot(x=data[column])
        plt.show()