#Cargar el archivo 'datos.csv' en un dataframe utilizando la función correspondiente de Pandas y muestra los primeros 10 registros.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datos.csv')
print(df.head(10))

#Calcular y mostrar la desviación estándar de las calificaciones.

print(df['Edad'].std())


#Mostrar el número de estudiantes por cada edad utilizando un gráfico de barras.

df['Edad'].value_counts().plot(kind='bar')
plt.show()


#Mostrar la distribución de calificaciones utilizando un histograma.

df['Calificacion'].plot(kind='hist')
plt.show()


#Guardar el dataframe actualizado con una nueva columna que clasifique a los estudiantes como 'Suspenso' si su calificación es menor a 5, 'Aprobado' si su calificación es de 5 a 7 , 'Notable' si su calificación es entre 7 y 9 y 'Sobresaliente' por encima de 9.

def clasificacion(calificacion):
    if calificacion < 5:
        return 'Suspenso'
    elif calificacion >= 5 and calificacion < 7:
        return 'Aprobado'
    elif calificacion >= 7 and calificacion < 9:
        return 'Notable'
    else:
        return 'Sobresaliente'
    
df['Clasificacion'] = df['Calificacion'].apply(clasificacion)
print(df.head(10))


#Usa una función para encontar al alumno con la mejor calificación y cambiarle la nota por matrícula.

def matricula(calificacion):
    if calificacion == df['Calificacion'].max():
        return 'Matricula'
    else:
        return calificacion
    
df['Clasificacion'] = df['Calificacion'].apply(matricula)
print(df.head(10))






