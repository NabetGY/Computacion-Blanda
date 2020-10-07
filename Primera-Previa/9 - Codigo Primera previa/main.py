# COMPUTACIÓN BLANDA - Sistemas y Computación

# -----------------------------------------------------------------
# AJUSTES POLINOMIALES
# -----------------------------------------------------------------
# Lección 06
#
#   ** Se importan los archivos de trabajo
#   ** Se crean las variables
#   ** Se generan los modelos
#   ** Se grafican las funciones
#
# -----------------------------------------------------------------

# Se importa la librería del Sistema Operativo
# Igualmente, la librería utils y numpy
# -----------------------------------------------------------------
import os

# Directorios: chart y data en el directorio de trabajo
# DATA_DIR es el directorio de los datos
# CHART_DIR es el directorio de los gráficos generados
# -----------------------------------------------------------------
from utils import DATA_DIR, CHART_DIR
import numpy as np

# Se eliminan las advertencias por el uso de funciones que
# en el futuro cambiarán
# -----------------------------------------------------------------
np.seterr(all='ignore')

# Se importa la librería scipy y matplotlib
# -----------------------------------------------------------------
import scipy as sp
import matplotlib.pyplot as plt

# Datos de trabajo
# -----------------------------------------------------------------
data = np.genfromtxt(os.path.join(DATA_DIR, "Datos-Café.tsv"), 
                     delimiter="\t")

# Se establece el tipo de dato
data = np.array(data, dtype=np.float64)
print(data[:10])
print(data.shape)

# Se definen los colores
# g = green, k = black, b = blue, m = magenta, r = red
# g = verde, k = negro, b = azul, m = magenta, r = rojo
colors = ['g', 'k', 'b', 'm', 'r']

# Se definen los tipos de líneas
# los cuales serán utilizados en las gráficas
linestyles = ['-', '-.', '--', ':', '-']

# Se crea el vector x, correspondiente a la primera columna de data
# Se crea el vercot y, correspondiente a la segunda columna de data
x = data[:, 0]
y = data[:, 1]

# la función isnan(vector) devuelve un vector en el cual los TRUE
# son valores de tipo nan, y los valores FALSE son valores diferentes
# a nan. Con esta información, este vector permite realizar 
# transformaciones a otros vectores (o al mismo vector), y realizar
# operaciones como sumar el número de posiciones TRUE, con lo
# cual se calcula el total de valores tipo nan
print("Número de entradas incorrectas:", np.sum(np.isnan(y)))

# Se eliminan los datos incorrectos
# -----------------------------------------------------------------

# Los valores nan en el vector y deben eliminarse
# Para ello se crea un vector TRUE y FALSE basado en isnan
# Al negar dichos valores (~), los valores que son FALSE se vuelven
# TRUE, y se corresponden con aquellos valores que NO son nan
# Si el vector x, que contiene los valores en el eje x, se afectan
# a partir de dicho valores lógicos, se genera un nuevo vector en
# el que solos se toman aquellos que son TRUE. Por tanto, se crea
# un nuevo vector x, en el cual han desaparecido los correspondientes
# valores de y que son nan

# Esto mismo se aplica, pero sobre el vector y, lo cual hace que tanto
# x como y queden completamente sincronizados: sin valores nan
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

# CON ESTA FUNCIÓN SE DEFINE UN MODELO, EL CUAL CONTIENE 
# el comportamiento de un ajuste con base en un grado polinomial
# elegido
# -----------------------------------------------------------------
def plot_models(x, y, models, fname, mx=None, ymax=None, xmin=None):
    ''' dibujar datos de entrada '''

    # Crea una nueva figura, o activa una existente.
    # num = identificador, figsize: anchura, altura
    plt.figure(num=None, figsize=(8, 6))
    
    # Borra el espacio de la figura
    plt.clf()
    
    # Un gráfico de dispersión de y frente a x con diferentes tamaños 
    # y colores de marcador (tamaño = 10)
    plt.scatter(x, y, s=10)
    
    # Títulos de la figura
    # Título superior
    plt.title("Valor de las exportaciones del café colombiano \n")
    
    # Título en la base
    plt.xlabel("Años")

 
    # Título lateral
    plt.ylabel("Millones de dólares")
    
    # Obtiene o establece las ubicaciones de las marcas 
    # actuales y las etiquetas del eje x.
    
    # Los primeros corchetes ([]) se refieren a las marcas en x
    # Los siguientes corchetes ([]) se refieren a las etiquetas
    
    # En el primer corchete se tiene: 1*7*24 + 2*7*24 + ..., hasta
    # completar el total de puntos en el eje horizontal, según
    # el tamaño del vector x
    
    # Además, se aprovecha para calcular los valores de w, los
    # cuales se agrupan en paquetes de w*7*24. Esto permite
    # determinar los valores de w desde 1 hasta 5, indicando
    # con ello que se tiene un poco más de 4 semanas
  
    # Estos valores se utilizan en el segundo corchete para
    # escribir las etiquetas basadas en estos valores de w
    
    # Por tanto, se escriben etiquetas para w desde 1 hasta
    # 4, lo cual constituye las semanas analizadas
    plt.xticks(
        [w * 60 for w in range(5)], 
        ['%i' % (2000+w*5) for w in range(5)])

    # Aquí se evalúa el tipo de modelo recibido
    # Si no se envía ninguno, no se dibuja ninguna curva de ajuste
    if models:
        
        # Si no se define ningún valor para mx (revisar el 
        # código más adelante), el valor de mx será
        # calculado con la función linspace

        # NOTA: linspace devuelve números espaciados uniformemente 
        # durante un intervalo especificado. En este caso, sobre
        # el conjunto de valores x establecido
        if mx is None:
            mx = np.linspace(0, 264, 1000)       
        # La función zip () toma elementos iterables 
        # (puede ser cero o más), los agrega en una tupla y los devuelve

# HASTA AQUÍ ESTÁ RESUELTO

# --------------------------------------------------------------------

# AQUÍ INICIA LA TAREA DE DOCUMENTACIÓN

# --------------------------------------------------------------------
        
        # Aquí se realiza un ciclo .....
        
        for model, style, color in zip(models, linestyles, colors):
            # print "Modelo:",model
            # print "Coeffs:",model.coeffs
            
            # Permite incluir varias gráficas en una única figura
            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
            
            
        # Coloca leyendas en los ejes.
        plt.legend(["d=%i" % m.order for m in models], loc="upper left")
        
    
    # Establece las margenes en cero 
    plt.autoscale(tight=True)
    # Obtiene o establece los límites y de los ejes actuales.
    plt.ylim(ymin=0)
    
    # Si ymax es diferente de cero se establece el limite maximo del eje y
    if ymax:
        plt.ylim(ymax=ymax)
        
    # Si xmin es diferente de cero se establece el limite minimo del eje x
    if xmin:
        plt.xlim(xmin=xmin)
        
    # Se establece valores para la cuadricula, es visible, estilo de linea solido, y con una opacidad de 75%
    plt.grid(True, linestyle='-', color='0.75')
    
    # Guardamos el grafico
    plt.savefig(fname)

# Primera mirada a los datos
# -----------------------------------------------------------------
plot_models(x, y, None, os.path.join(CHART_DIR, "1400_01_01.png"))

# Crea y dibuja los modelos de datos
# -----------------------------------------------------------------

#Ajuste polinomial de mínimos cuadrados.
#Ajuste un polinomio de grado 1 a los puntos (x, y) .
#Devuelve un vector de coeficientes p que minimiza el error al cuadrado en el orden deg , deg-1 ,… 0
fp1, res1, rank1, sv1, rcond1 = np.polyfit(x, y, 1, full=True)
print("Parámetros del modelo fp1: %s" % fp1)
print("Error del modelo fp1:", res1)

#Esta función ayuda a definir una función polinomial. 
#Facilita la aplicación de "operaciones naturales" en polinomios.
f1 = sp.poly1d(fp1)

#Ajuste un polinomio de grado 2 a los puntos (x, y) .
#Devuelve un vector de coeficientes p que minimiza el error al cuadrado en el orden deg , deg-1 ,… 0
fp2, res2, rank2, sv2, rcond2 = np.polyfit(x, y, 2, full=True)
print("Parámetros del modelo fp2: %s" % fp2)
print("Error del modelo fp2:", res2)

#Esta función ayuda a definir una función polinomial. 
#Facilita la aplicación de "operaciones naturales" en polinomios.
f2 = sp.poly1d(fp2)

#Ajuste un polinomio de grado 3 a los puntos (x, y) 
f3 = sp.poly1d(np.polyfit(x, y, 3))

#Ajuste un polinomio de grado 4 a los puntos (x, y) 
fp4, res4, rank4, sv4, rcond4 = np.polyfit(x, y, 4, full=True)
print("Parámetros del modelo fp4: %s" % fp4)
print("Error del modelo fp4:", res4)
f4 = sp.poly1d(fp4)

#Ajuste un polinomio de grado 5 a los puntos (x, y) 
f5 = sp.poly1d(np.polyfit(x, y, 5))
# Se grafican los modelos'''
# -----------------------------------------------------------------
plot_models(x, y, [f1], os.path.join(CHART_DIR, "1400_01_02.png"))
plot_models(x, y, [f1, f2], os.path.join(CHART_DIR, "1400_01_03.png"))
plot_models(x, y, [f1, f2, f3], os.path.join(CHART_DIR, "1400_01_04.png"))
plot_models(x, y, [f1, f2, f3, f4], os.path.join(CHART_DIR, "1400_01_05.png"))
plot_models(x, y, [f1, f2, f3, f4, f5], os.path.join(CHART_DIR, "1400_01_06.png"))

plot_models(x, y, [f5], os.path.join(CHART_DIR, "1400_01_07.png"))


#-----------------------------------------------------------------
# Se hace la prediccion en el mes 264, ultimo mes del año 2022
P= f4(264)
print("\nPara el ultimo mes del año 2022 se exportaran $", round(P,2), "millones de dólares de café colombiano")