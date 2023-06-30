#Cargar el archivo 'datos.csv' en un dataframe utilizando la función correspondiente de Pandas y muestra los primeros 10 registros.
#Calcular y mostrar la desviación estándar de las calificaciones.
#Mostrar el número de estudiantes por cada edad utilizando un gráfico de barras.
#Mostrar la distribución de calificaciones utilizando un histograma.
#Guardar el dataframe actualizado con una nueva columna que clasifique a los estudiantes como 'Suspenso' si su calificación es menor a 5, 'Aprobado' si su calificación es de 5 a 7 , 'Notable' si su calificación es entre 7 y 9 y 'Sobresaliente' por encima de 9.
#Usa una función para encontar al alumno con la mejor calificación y cambiarle la nota por matrícula.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("datos.csv")
print(df.head(10))
print(df["Calificacion"].std())
print(df["Edad"].value_counts().plot(kind="bar"))
print(df["Calificacion"].plot(kind="hist"))
df["Clasificacion"] = np.where(df["Calificacion"] < 5,"Suspenso",np.where(df["Calificacion"] < 7,"Aprobado",np.where(df["Calificacion"] < 9,"Notable","Sobresaliente")))
print(df)
df.loc[df["Calificacion"].idxmax(),"Calificacion"] = "Matricula"
print(df)


