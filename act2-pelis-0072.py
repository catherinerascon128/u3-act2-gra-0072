import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# catherine eileen huerta rascon NC = 0072
# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
# Problema 6: Películas (Título, recaudación en billones USD, ganó Oscar a mejor película, año)
avt = ['Avatar', 2.9, False, 2009]
end = ['Avengers: Endgame', 2.7, False, 2019]
ttn = ['Titanic', 2.2, True, 1997]
sw7 = ['Star Wars VII', 2.0, False, 2015]
inf = ['Avengers: Infinity War', 2.0, False, 2018]
# creamos una lista de listas (conformando la tabla)
lista_peliculas=[avt,end,ttn,sw7,inf]
# print(lista_redes_sociales)
# utilizar pandas para organizar a tabla (dataframe o marco de datos)
# a cada columna le ponemos nombre
df_peliculas=pd.DataFrame(lista_peliculas,columns=["Nombre","Cantidad","es_FB","Año"])
print(df_peliculas)
# creamos el archivo CSV y lo guardamos en CSV
df_peliculas.to_csv("peliculas.csv", index=False)
# crear graficas de lineas 
# donde x es Nombre en el eje horizontal
# donde y es Cantidad en el eje vertical
plt.plot(df_peliculas["Nombre"],df_peliculas["Cantidad"])
plt.title("grafica peliculas 0072")
plt.xlabel("nombre de las peliculas")
plt.ylabel("cantidad de peliculas")
plt.show()
# creamos una grafica de puntos
plt.scatter(df_peliculas["Nombre"],df_peliculas["Cantidad"])
plt.show()
# grafica de barras
plt.bar(df_peliculas["Nombre"],df_peliculas["Cantidad"])
plt.title("pelis 0072")
plt.xlabel("peliculas")
plt.ylabel("Cantidad de pelis")
plt.show()
# ordenar la grafica de barras de manera desencente 
# de la mas grande a la mas pequeña
df_rs_ordenar=df_peliculas.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# coloreando la grafica 
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()
# grafica de pastel 
plt.plot(df_peliculas["Nombre"],df_peliculas["Cantidad"])
plt.pie(df_peliculas["Cantidad"],labels=df_peliculas["Nombre"])
plt.show()
print("catherine eileen huerta rascon NC = 0072")