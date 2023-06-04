import pandas as pd
                                                    # el formato es import "librería" as "nombre con el la queremos llamar".
import matplotlib.pyplot as plt
                                                    # matplotlib es una librería para hacer gráficos.
import numpy as np
                                                    # numpy es una librería para hacer cuentas de forma eficiente.
import matplotlib.gridspec as gridspec
                                                    # gridspec es una libreria que permite hacer
import seaborn as sb
                                                    # libreria para grafico de barras.
import scipy as sc

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
                                                    #esta celda permite saltar errores de certificados de las páginas que contienen los datos
URL = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/agencia-de-proteccion-ambiental/calidad-aire/calidad-aire.csv"

data_base = pd.read_csv(URL)
                                                    #leo la base de datos

data_base['FECHA'] = pd.to_datetime(data_base['FECHA'], format='%d%b%Y:%H:%M:%S')
                                                    # cambio los datos de la columna fecha a datos tipo datetime

data_2022 = data_base[data_base['FECHA'].dt.year == 2022]
                                                    # creo una base de datos solo con los valores del año 2022

data_2022['FECHA'] = pd.to_datetime(data_2022['FECHA'], format='%d%m%Y:%H:%M:%S')
                                                    # cambio los datos de la columna fecha a datos tipo datetime

data_2022 = data_2022.sort_values("FECHA")

data_2022 = data_2022[data_2022['CO_CENTENARIO'] != 'nan']
data_2022 = data_2022[data_2022['CO_CENTENARIO'] != 's/d']
                                                    #filtro las filas de las base de datos donde CO centenario tenga un campo vacio o un s/d

#data_final = data_2022.drop_duplicates(subset='FECHA', keep='first')
                                                    #elimino las fechas repetidas, esto se podria mejorar calculando la media del dia

print ("base de datos filtrada con los datos finales")
print (data_2022)
data_2022 = data_2022.astype(str)

# data_final.CO_CENTENARIO = data_final.CO_CENTENARIO.astype(float)
# print ("datos estadisticos de la columna CO_Centanerio")
# print(data_final.CO_CENTENARIO.describe())
# data_final.CO_CENTENARIO = data_final.CO_CENTENARIO.astype(str)
# print(data_final.CO_CENTENARIO)



                                                    #Histograma
#
#
#
# fig2 = plt.figure(figsize=(9, 5))
#                                                     # Tamaño de la figura
# #niveles = [0, 0.20, 0.40, 0.60, 0.80, 1, 1.20, 1.40, 1.60, 1.80, 2, 2.20, 2.40]
# plt.hist(data_final['CO_CENTENARIO'], ec="red")
#                                                     # la libreria plt tiene a ".hist" que genera un histograma
#                                                     # de la columna guardada en la variable "atributo".
#                                                     # bins: número de intervalos en los que se divide el rango.
# plt.xlabel('Niveles de monoxido de carbono -CO')
# #plt.xlim(0, 2.4)  # Establecer límites del eje x
# #plt.xticks(niveles)  # Establecer las marcas en el eje x

# plt.ylabel('Cantidad de dias en el año')
#                                                     # etiqueta eje y
# fig2.suptitle('Histograma del monoxido de carbono en la estacion Centenario')
# #título
# #plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left') # posición del título
# plt.show()



                                                    #Grafico plot
plt.plot(data_2022.FECHA[::7], data_2022.CO_CENTENARIO[::7])
plt.xlabel("Fecha")
plt.ylabel("Monóxido de Carbono")
plt.title("Niveles de Monóxido de Carbono en 2022")
plt.xticks(rotation=45)
plt.show()