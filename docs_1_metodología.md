## 1. Métodos y Datos Utilizados

### 1.1 Datos Utilizados

Los datos para este estudio se extrajeron de **12 estaciones meteorológicas** del Sistema de Información Agroclimática para el Riego (SIAR). La información recopilada incluye **temperaturas** (máximas, mínimas y medias diarias), **humedad relativa**, **radiación solar** y **velocidades del viento**, entre otros. Además, se incluyen valores diarios de $ET_0$ calculados según el método de la FAO-Penman Monteith.

Cada estación proporcionó la mayor cantidad posible de datos, resultando en un número variable de registros totales debido a diferencias en el inicio de la recolección de datos y al estado de actividad de las estaciones.

La Tabla 1 detalla el **período disponible** y los **datos geográficos** de las estaciones consideradas. Se considera que los datos de estas estaciones son climáticamente normales, sin fluctuaciones drásticas en las variables. Se descartaron los datos de variables que excedían $\pm 3$ desviaciones estándar del valor medio.

| Estación        | Período disponible | Días Totales | UTM X   | UTM Y   | Altitud (m) |
| :-------------- | :----------------- | :----------- | :------ | :------ | :---------- |
| 1 Artà          | 2005-2017          | 4022         | 1045510 | 4413540 | 114         |
| 2 Calvià        | 2005-2017          | 3999         | 969620  | 4392240 | 20          |
| 3 Ciutadella    | 2008-2009          | 240          | 1085510 | 4446460 | 21          |
| 4 Eivissa S'estany | 2005-2017          | 3957         | 882360  | 4295680 | 11          |
| 5 Es Mercadal   | 2005-2017          | 4142         | 1106140 | 4452380 | 41          |
| 6 Felanitx      | 2004-2017          | 4786         | 1023670 | 4387260 | 109         |
| 7 Inca          | 2004-2017          | 4784         | 1009420 | 4409550 | 42          |
| 8 Manacor       | 2004-2017          | 4764         | 1030470 | 4395600 | 84          |
| 9 Santa Eulàlia | 2004-2017          | 4631         | 884487  | 4327280 | 130         |
| 10 Sa Pobla     | 2004-2017          | 4756         | 1017420 | 4423370 | 6           |
| 11 Sóller       | 2004-2012          | 2878         | 989206  | 4419030 | 44          |
| 12 Son Ferriol  | 2004-2017          | 4704         | 992040  | 4394870 | 28          |

**Tabla 1: Datos de las estaciones**

La Tabla 2 presenta los valores medios de diferentes variables medidas por las estaciones, mientras que la Tabla 3 muestra las desviaciones estándar de cada variable por estación.

| Estación | Temp Media (°C) | Temp Max (°C) | Temp Mínima (°C) | Humedad Media (%) | Humedad Max (%) | Humedad Min (%) | Vel. del viento (m/s) | Vel. del viento Max (m/s) | Radiación (MJ/m²) | Radiación extraterrestre calculada(MJ/m²) |
| :------- | :-------------- | :------------ | :--------------- | :---------------- | :-------------- | :-------------- | :-------------------- | :------------------------ | :---------------- | :---------------------------------------- |
| 1        | 16.37           | 22.38         | 10.76            | 76.20             | 95.03           | 49.57           | 0.80                  | 4.58                      | 15.60             | 28.30                                     |
| 2        | 16.73           | 22.97         | 10.59            | 75.24             | 94.22           | 48.82           | 1.02                  | 5.04                      | 15.63             | 28.09                                     |
| 3        | 16.09           | 20.17         | 11.63            | 76.07             | 92.68           | 54.84           | 2.11                  | 6.69                      | 18.07             | 30.09                                     |
| 4        | 18.54           | 21.82         | 14.99            | 75.35             | 90.00           | 57.56           | 2.52                  | 6.83                      | 16.91             | 28.45                                     |
| 5        | 17.16           | 22.33         | 11.81            | 74.83             | 93.05           | 51.16           | 1.14                  | 5.38                      | 15.31             | 28.53                                     |
| 6        | 17.13           | 23.56         | 11.33            | 74.15             | 93.97           | 46.00           | 0.98                  | 5.30                      | 16.27             | 28.76                                     |
| 7        | 16.78           | 23.61         | 10.22            | 73.46             | 94.60           | 44.71           | 1.66                  | 6.36                      | 16.80             | 28.71                                     |
| 8        | 16.67           | 23.16         | 10.23            | 74.91             | 94.70           | 46.80           | 1.66                  | 6.48                      | 16.54             | 28.77                                     |
| 9        | 17.07           | 23.14         | 10.92            | 74.86             | 94.95           | 47.44           | 1.41                  | 6.08                      | 16.78             | 29.32                                     |
| 10       | 16.50           | 23.65         | 9.28             | 76.08             | 95.62           | 47.70           | 1.28                  | 6.04                      | 16.04             | 28.70                                     |
| 11       | 17.20           | 23.10         | 11.73            | 72.48             | 92.32           | 46.15           | 0.45                  | 3.74                      | 13.85             | 28.36                                     |
| 12       | 17.47           | 23.67         | 11.53            | 74.15             | 92.90           | 47.72           | 1.09                  | 5.08                      | 16.12             | 28.75                                     |

**Tabla 2: Valores medios de diferentes variables de las estaciones**

| Estación | Temp Media (°C) | Temp Max (°C) | Temp Mínima (°C) | Humedad Media (%) | Humedad Max (%) | Humedad Min (%) | Vel. del viento (m/s) | Vel. del viento Max (m/s) | Radiación (MJ/m²) | Radiación extraterrestre calculada(MJ/m²) |
| :------- | :-------------- | :------------ | :--------------- | :---------------- | :-------------- | :-------------- | :-------------------- | :------------------------ | :---------------- | :---------------------------------------- |
| 1        | 5.89            | 6.64          | 5.60             | 10.27             | 5.39            | 13.75           | 0.46                  | 1.48                      | 7.91              | 10.06                                     |
| 2        | 5.80            | 6.36          | 5.71             | 10.35             | 6.04            | 13.34           | 0.48                  | 1.95                      | 7.77              | 10.01                                     |
| 3        | 6.23            | 6.99          | 6.06             | 9.42              | 5.71            | 14.76           | 1.02                  | 2.17                      | 8.94              | 10.73                                     |
| 4        | 5.14            | 5.67          | 5.08             | 9.31              | 7.35            | 12.43           | 1.20                  | 2.20                      | 8.10              | 9.92                                      |
| 5        | 5.83            | 6.73          | 5.55             | 9.60              | 5.59            | 13.22           | 0.76                  | 1.78                      | 8.25              | 10.12                                     |
| 6        | 6.38            | 7.06          | 6.10             | 11.13             | 5.45            | 14.90           | 0.51                  | 1.59                      | 7.88              | 9.98                                      |
| 7        | 6.39            | 7.40          | 5.92             | 11.32             | 5.18            | 15.13           | 0.85                  | 2.01                      | 8.33              | 10.07                                     |
| 8        | 6.22            | 6.93          | 5.93             | 10.33             | 4.62            | 14.53           | 0.85                  | 2.09                      | 8.07              | 10.03                                     |
| 9        | 6.07            | 6.75          | 5.96             | 10.23             | 5.17            | 14.22           | 0.68                  | 1.82                      | 8.09              | 9.87                                      |
| 10       | 6.08            | 6.87          | 5.84             | 10.04             | 4.44            | 14.69           | 0.73                  | 2.26                      | 8.07              | 10.06                                     |
| 11       | 6.35            | 6.99          | 5.86             | 11.62             | 6.97            | 13.13           | 0.28                  | 1.44                      | 8.56              | 10.00                                     |
| 12       | 6.20            | 6.66          | 6.19             | 10.46             | 6.10            | 14.64           | 0.56                  | 1.69                      | 7.62              | 9.96                                      |

**Tabla 3: Desviaciones estándar de diferentes variables de las estaciones**

---

### 1.2 Cálculo de Targets

La aplicación de las Redes Neuronales Artificiales (ANNs) requiere **valores objetivo o "targets"** para entrenar y validar los modelos. Dado que las mediciones directas con lisímetros son complejas y costosas de automatizar, los datos de $ET_0$ utilizados como targets para entrenar los modelos neuronales se calcularon con el modelo de la **FAO-56 PM**, considerado el método estándar para su cálculo.

$$ET_0 = \frac{0.409 \Delta (R_n - G) + \gamma \frac{900}{T+273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)} \quad (1)$$

Como se observa en la ecuación (1), la ecuación de Penman-Monteith (PM) proporciona el resultado en ($mm/día$). Aquí, $R_n$ es la radiación neta en la superficie del cultivo ($MJ m^{-2} día^{-1}$), $G$ es el flujo de calor del suelo ($MJ m^{-2} día^{-1}$), $T$ es la temperatura media diaria del aire a 2 metros de altura (°C), $\gamma$ es la constante psicométrica ($kPa/°C$), $\Delta$ es la pendiente de la curva de la presión de vapor ($kPa/°C$), $e_s$ es la presión de vapor de saturación ($kPa$), $e_a$ es la presión de vapor real ($kPa$) y $u_2$ es la velocidad del viento a 2 metros de altura ($m/s$).

Aunque las estaciones ya proporcionaban el valor de $ET_0$ calculado con el modelo PM, se procedió a recalcularlo para verificar su exactitud y utilizarlo como referencia de salida (output) en el entrenamiento de las redes neuronales, siguiendo el procedimiento de Allen et al. (1998).

---

### 1.3 Aplicación de Redes Neuronales Artificiales

#### 1.3.1 Funcionamiento de la Red y su Entrenamiento

El funcionamiento de las redes neuronales más comunes se basa en **aprender de los errores** generados a partir de unas entradas (inputs) y una salida de referencia (output), para reajustar progresivamente los parámetros del modelo.

La arquitectura de una red neuronal consta de una capa de entrada, una o varias capas ocultas y una capa de salida, con un número determinado de neurones en cada capa. Las redes neuronales utilizadas y entrenadas siguen el **algoritmo de retropropagación del error**. La retropropagación es un método de aprendizaje supervisado que permite **reajustar los pesos** asignados inicialmente de forma aleatoria, reduciendo gradualmente el error en cada iteración hasta alcanzar un error mínimo respecto al output deseado. Los outputs generados por la red se comparan con los targets, generando errores que se propagan hacia atrás para ajustar los pesos mediante un algoritmo que busca minimizar la función de error elegida, comúnmente el Error Cuadrático Medio (MSE).



Todas las neuronas utilizadas siguen la configuración del modelo de Haykin (1999), calculando sus valores de salida mediante las siguientes fórmulas:

$$Z = \sum_{k=1}^{N} w_k x_k + b \quad (2)$$
$$y = f(Z) \quad (3)$$

Donde $x_k$ es la señal de entrada, $w_k$ es el peso sináptico de la neurona k, $Z$ es el combinador lineal o suma ponderada, $b$ es el término independiente o "bias", $y$ es la salida de la neurona y $f$ es la función de transferencia. La Figura 9 representa el funcionamiento de estas neuronas.

#### 1.3.2 Error Evaluado en el Entrenamiento

La función de error elegida para el criterio de entrenamiento ha sido el **Error Cuadrático Medio (MSE)**. El objetivo es obtener el valor mínimo posible al sumar los errores cuadráticos de las neuronas de salida. La fórmula para el cálculo del MSE es:

$$MSE = \frac{1}{N} \sum_{n=1}^{N} e_n^2 \quad (4)$$

Donde $N$ es el número de iteraciones/patrones y $e_n$ es el error cometido por la red para el n-ésimo patrón/iteración, dado por:

$$e_n = y_n - t_n \quad (5)$$

Donde $y_n$ y $t_n$ son los vectores de salida de la red y la salida deseada para el n-ésimo patrón, respectivamente.

#### 1.3.3 Función de Transferencia

La función de transferencia o activación introduce **no linealidad** en la suma ponderada de cada neurona. En este estudio se eligió la función **tangente sigmoidal (tansig)**, a diferencia de la función de activación logsig. Estudios previos han utilizado esta función de activación con éxito en conjuntos de datos similares (Martí y Gasque 2010; Martí et al. 2010a, c).

#### 1.3.4 Algoritmo de Aprendizaje

El algoritmo elegido para reajustar los pesos del modelo neuronal ha sido el de **Levenberg-Marquardt**. Este algoritmo muestra **velocidades de convergencia rápidas** del MSE, a pesar de la complejidad de su cálculo, que se realiza mediante la matriz Jacobiana de los errores de las neuronas de salida.

$$\Delta w = -[J^T J + \mu I]^{-1} J^T e \quad (6)$$

Donde $J$ es la matriz Jacobiana de los errores de las neuronas de salida, $J^T$ es su transpuesta, $I$ es la matriz identidad del mismo tamaño que la matriz Jacobiana, $e$ es el vector de errores de las neuronas de salida y $\mu$ es una constante que decrece en cada iteración si se observa una reducción del MSE, o se incrementa si los pesos actualizados aumentan el MSE. Este algoritmo está implementado en el software Matlab.

#### 1.3.5 Criterio de Parada del Aprendizaje

Un problema en la implementación de modelos neuronales es que tienden a ajustarse excesivamente a los datos de entrenamiento, perdiendo capacidad de generalización con datos nuevos. Para evitar el fenómeno de **sobreajuste (overfitting)**, se aplicó la técnica de **parada anticipada (early stopping)**.

Este método consiste en separar una parte de los datos (15% de los datos de entrenamiento) como **conjunto de datos de validación cruzada (CV)**. Este conjunto se utiliza para controlar el grado de sobreajuste. El entrenamiento se detiene cuando el error en el conjunto de CV deja de disminuir. Se estableció un límite máximo de 100 iteraciones para evitar cargas de tiempo excesivas.

#### 1.3.6 Partición de Datos

Se eligió la técnica de **validación cruzada (k-fold)** para dividir el conjunto de datos. En este método, el conjunto de datos se divide en varias particiones. En cada partición, una parte se utiliza para entrenamiento y la restante para testear el modelo. Este proceso se repite, utilizando un conjunto de datos diferente para testear en cada etapa, hasta evaluar el conjunto completo. El error se calcula como la media de los resultados de cada combinación. Para este estudio, los datos se dividieron por años, reservando un año para testeo y utilizando los restantes para entrenamiento. Se crearon matrices de entrenamiento (Tr), validación (CV) y test (Te) para cada combinación.

#### 1.3.7 Arquitectura Óptima

No existe un criterio único para definir la arquitectura óptima de una ANN; suele determinarse por prueba y error. En este trabajo, se estableció **una sola capa oculta** con un máximo de 10 neuronas. Se entrenaron redes con 1 a 10 neuronas, repitiendo el proceso de aprendizaje 10 veces por cada arquitectura para mitigar el efecto de la asignación aleatoria inicial de pesos. Se seleccionaron dos modelos: uno con el menor error de validación (mayor capacidad de generalización) y otro con el menor error de test.

#### 1.3.8 Inputs Considerados

La selección de los inputs para los modelos neuronales es crucial para evitar la introducción de ruido y mejorar la estimación de la $ET_0$. Se entrenaron diferentes modelos con distintas combinaciones de inputs, justificadas por fórmulas empíricas existentes. La Tabla 4 presenta las combinaciones de inputs elegidas.

| Modelo Neuronal/Empírico | Nombre Red | Nombre Modelo Empírico | Nº Inputs | Inputs                                       | Output |
| :----------------------- | :--------- | :--------------------- | :-------- | :------------------------------------------- | :----- |
|                          |            |                        | 2         | Rs, Tmitja                                   |        |
|                          |            |                        | 4         | Tmax, Tmin, Tmitja, Ra                       |        |
|                          |            |                        | 5         | Tmax, Tmin, Tmitja, Ra, HR mitja             |        |

**Tabla 4: Modelos considerados en el estudio y sus respectivos inputs**

#### 1.3.9 Modelos Neuronales Implementados

Se analizaron un total de **43,800 modelos neuronales**, considerando las diferentes estaciones, años, arquitecturas, repeticiones y combinaciones de inputs. La Tabla 5 resume el balance de modelos analizados.

| Estación | Años | Neuronas | Repeticiones | Combinaciones de inputs | Total   |
| :------- | :--- | :------- | :----------- | :---------------------- | :------ |
| 1        | 13   | 10       | 10           | 3                       | 3900    |
| 2        | 13   | 10       | 10           | 3                       | 3900    |
| 3        | 2    | 10       | 10           | 3                       | 600     |
| 4        | 13   | 10       | 10           | 10                      | 3900    |
| 5        | 13   | 10       | 10           | 10                      | 3900    |
| 6        | 13   |  10      | 10           | 10                      | 3900    |
| 7        | 14   | 10       | 10           | 10                      | 4200    |
| 8        | 14   | 10       | 10           | 10                      | 4200    |
| 9        | 14   | 10       | 10           | 10                      | 4200    |
| 10       | 14   |  10      | 10           | 10                      | 4200    |
| 11       | 9    |  10      | 10           | 10                      | 2700    |
| 12       | 14   |  10      | 10           | 10                      | 4200    |
| **Total**|      |          |              |                         | **43,800** |

**Tabla 5: Balance de modelos neuronales considerados**

---

### 1.4 Fórmulas Empíricas

Los inputs seleccionados para cada caso se basan en las siguientes fórmulas empíricas para calcular la evapotranspiración.

#### 1.4.1 Ecuación Original de Hargreaves

Hargreaves (1985) propuso una ecuación para predecir la $ET_0$ basándose únicamente en la radiación solar ($R_s$) y la temperatura media ($T$).

$$ET_0 = 0.0023 R_a (T + 17.8) (T_{max} - T_{min})^{0.5} \quad (7)$$

Donde $R_a$ es la radiación extraterrestre. Si bien $R_s$ estaba medida, la dependencia de $R_a$ hace que esta ecuación no siempre sea aplicable si $R_a$ no está disponible.

#### 1.4.2 Ecuación de Hargreaves y Samani

Hargreaves y Samani (1982) concluyeron que la fracción de radiación extraterrestre que llega a la superficie terrestre puede estimarse mediante la diferencia de temperatura máxima y mínima. Propusieron la siguiente fórmula:

$$ET_0 = 0.0023 R_a (T + 17.8) (T_{max} - T_{min})^{0.5} \quad (8)$$

Donde $R_a$ es la radiación extraterrestre. El coeficiente empírico (originalmente 0.17 para regiones semiáridas) se ajusta según la región.

Basándose en la ecuación anterior y en la relación entre radiación solar y extraterrestre, Hargreaves y Samani (1985) desarrollaron una ecuación que solo requiere temperatura, día del año y latitud:

$$ET_0 = 0.0023 R_a (T + 17.8) (T_{max} - T_{min})^{0.5} \quad (9)$$

El cálculo de $R_a$ se extrae de Allen et al. (1998) y depende de la distancia Tierra-Sol, el ángulo de radiación al atardecer, la latitud y la declinación solar.

$$R_a = \frac{24 \times 60}{\pi} G_{sc} [d_r (\omega_s \sin(\phi) \sin(\delta) + \cos(\phi) \cos(\delta) \sin(\omega_s))] \quad (10)$$

Donde $G_{sc}$ es la constante solar ($0.082 MJ m^{-2} min^{-1}$), $d_r$ es la distancia relativa inversa Tierra-Sol, $\omega_s$ es el ángulo de radiación a la puesta del sol en radianes, $\phi$ es la latitud y $\delta$ es la declinación solar en radianes.

$$d_r = 1 + 0.033 \cos(\frac{2\pi J}{365}) \quad (11)$$$$\delta = 0.409 \sin(\frac{2\pi J}{365} - 1.39) \quad (12)$$$$\omega_s = \sqrt{\frac{15(90 - \phi_{max})}{\pi}} \quad (13)$$$$ \phi_{max} = \arccos(-\tan(\delta) \tan(\phi)) \quad (14)$$

Donde $J$ es el día juliano.

#### 1.4.3 Ecuación de Valiantzas

Valiantzas (2017) propuso una fórmula para estimar la radiación solar a partir de datos de humedad relativa (RH):

$$R_s = R_a \left[a + b \frac{RH_{min}}{100} \right] \quad (15)$$

Donde los coeficientes $a$ y $b$ son empíricos. Combinando esta fórmula con la de Hargreaves, se obtiene una ecuación para el cálculo de $ET_0$:

$$ET_0 = 0.0023 R_a (T + 17.8) (T_{max} - T_{min})^{0.5} \quad (16)$$

Donde $RH$ es la humedad relativa.

#### 1.4.4 Ajuste de las Fórmulas Empíricas

Las tres fórmulas empíricas fueron ajustadas con un coeficiente AHC específico, calibrando los resultados iniciales con los de Penman-Monteith:

$$AHC = \frac{\sum_{k=1}^{N} ET_{0,k}^{Ref}}{\sum_{k=1}^{N} ET_{0,k}^{Emp}} \quad (17)$$
$$ET_{0,k}^{Emp,adj} = AHC \times ET_{0,k}^{Emp} \quad (18)$$

Donde $ET_{0,k}^{Ref}$ y $ET_{0,k}^{Emp}$ son los valores de evapotranspiración de referencia diaria calculados con Penman-Monteith y la fórmula empírica, respectivamente. Se extrae un coeficiente AHC para cada estación y fórmula. El ajuste se realiza para que las redes neuronales no tengan una ventaja al compararse con modelos empíricos no calibrados.

---

### 1.5 Evaluación de los Modelos

El rendimiento de los modelos se evaluó mediante varios indicadores, considerando los valores calculados de $ET_0$ con Penman-Monteith como referencia:

* **MSE (Mean Squared Error)**: Error cuadrático medio. Es la misma función de error utilizada en el entrenamiento de las redes neuronales.
    $$MSE = \frac{1}{N} \sum_{n=1}^{N} (y_n - t_n)^2 \quad (19)$$

* **RMSE (Root Mean Squared Error)**: Raíz cuadrada del error cuadrático medio.
    $$RMSE = \sqrt{\frac{1}{N} \sum_{n=1}^{N} (y_n - t_n)^2} \quad (20)$$

* **MAE (Mean Absolute Error)**: Error absoluto medio.
    $$MAE = \frac{1}{N} \sum_{n=1}^{N} |y_n - t_n| \quad (21)$$

* **Coeficiente de Determinación ($R^2$)**: Cuadrado del coeficiente de correlación de Pearson, mide la correlación lineal entre la estimación del modelo y los valores de referencia.

* **AARE (Average Absolute Relative Error)**: Media del error absoluto relativo.
    $$AARE = \frac{1}{N} \sum_{n=1}^{N} \left|\frac{y_n - t_n}{t_n}\right| \quad (23)$$

---

### 1.6 Implementación con Matlab
Traduzco y formateo en Markdown la información sobre los programas de Matlab utilizados en el estudio.

### 1.6 Implementación con Matlab

El software utilizado para la implementación de todos los modelos considerados ha sido **Matlab**. Matlab es una herramienta de software matemático que ofrece un entorno de desarrollo integrado con un lenguaje de programación propio.

Para que el programa integrado en Matlab pudiera entrenar las redes con los datos de las estaciones y de la manera deseada, se ha tenido que modificar la estructura original de los datos. Así, se pasó el formato de los datos de las estaciones a Matlab. Una vez implementados en el formato correspondiente de Matlab, es necesario darle a la base de datos cierta estructura para definir tanto el **k-fold** como los **inputs** de entrada de la red neuronal en cada caso.

Para llevar a cabo estas modificaciones, se han diseñado varios programas, definidos en la **Tabla 6**.

**Tabla 6: Programas implementados en Matlab**

| Nombre | Función | Inputs | Outputs | Página anexo |
|---|---|---|---|---|
| Depuradades | Elimina filas con `NaN` y valores que sobrepasan 3 veces la desviación media de las columnas de interés. | -Datos estaciones\<br\>-Vector fila con las columnas de interés | -Datos estaciones filtradas\<br\>-Datos eliminados | 55 |
| Mileni | Toma el conjunto de datos y resta 2000 a las columnas que corresponden al año. Ejemplo: "2005" pasa a ser "5". | -Datos estaciones | -Datos estaciones | 56 |
| Ordena2 | Divide el conjunto de datos de cada estación por años, organizando los datos por estaciones y, a su vez, cada estación por años. | -Datos estaciones | -Datos estaciones con una estructura de:\<br\>1-Estaciones\<br\>2-Años | 56 |
| Combinacions3 | Crea las combinaciones de años para cada estación, preparando la estructura "k-fold". Una combinación tendrá un año de prueba y el resto para entrenamiento. El programa solo crea las combinaciones, no las ejecuta. | -Datos estaciones | -Guía de combinaciones a seguir | 56 |
| Final | Utiliza las combinaciones extraídas del programa `Combinacions3` para separar el año de prueba del resto de años. Se tendrán tantas combinaciones como años de datos tenga cada estación. | -Datos estaciones\<br\>-Guía de combinaciones a seguir | -Conjunto de datos con una estructura de:\<br\>1-Estaciones\<br\>2-Combinaciones años\<br\>3-Año test / Años entrenamiento | 57 |
| Validació4 | Toma un porcentaje (%) de los datos de "training" para crear el conjunto de datos de validación. Por lo tanto, para cada combinación, se tendrá un año separado para prueba, un porcentaje de datos para validación cruzada y otro para entrenamiento. | -Datos estaciones\<br\>-Porcentaje de validación | -Conjunto de datos con una estructura de:\<br\>1-Estaciones\<br\>2-Combinaciones años\<br\>3-Año test / Años entrenamiento / Validación | 57 |
| Inout5 | Separa los **inputs** de los **outputs**. Dentro de cada conjunto de datos (test, training y cross validations), se separan las columnas de inputs y outputs. | -Datos estaciones\<br\>-Columnas inputs (en vector)\<br\>-Columna output | -Conjunto de datos con una estructura de:\<br\>1-Estaciones\<br\>2-Combinaciones años\<br\>3-Año test / Años entrenamiento / Validación\<br\>4-Inputs / Output | 57 |
| CONJUNT | Llama a los programas anteriores (`Mileni`, `Ordena2`, `Combinacions3`, `Final`, `Validació4`, `Inout5`) de forma sucesiva para automatizar el proceso de filtrado y preparación de la estructura de datos para el entrenamiento. | -Conjunto de inputs necesarios para los programas necesarios | -Conjunto de datos final con la estructura de `Inout5` | 58 |
| Prova1 | Es el programa principal, encargado de entrenar las redes neuronales. Incluye otros programas para obtener el resultado final, en la siguiente secuencia: `Filtra2`, `CONJUNT`, conversión de celdas a "estructura", `Entrenatesta1Talt`, `ANN1Talt`, cálculo de errores. | -Datos estaciones\<br\>-Porcentaje de datos de "Cross Validation"\<br\>-Número de neuronas máximas a entrenar\<br\>-Número de repeticiones\<br\>-Vector con las columnas de inputs\<br\>-Columna output\<br\>-Función de activación\<br\>-Número de capas ocultas | -Resultados finales:\<br\>· Errores globales (Criterio de Validación)\<br\>· Errores por estación (Criterio de Validación)\<br\>· Errores globales (Criterio de Prueba)\<br\>· Errores por estación (Criterio de Prueba) | 58 |
| Hgp2 | Calcula los valores de $ET\_0$ con las tres fórmulas diferentes. Primero, calcula la radiación extraterrestre con los datos de las estaciones y la latitud. Luego, calcula los valores de evapotranspiración y sus errores respecto a PM. También ajusta las ecuaciones de Hargreaves de forma anual extrayendo un coeficiente AHC para ajustar los resultados y volver a calcular los errores. | -Datos estaciones\<br\>-Latitudes de cada estación | -Valores diarios de $ET\_0$ con las diferentes fórmulas para cada estación.\<br\>-Errores respecto a PM\<br\>-Valores diarios de $ET\_0$ ajustados con AHC\<br\>-Errores de los valores ajustados respecto a PM | 61 |
| Estandard | Calcula la media y la desviación estándar de las variables climáticas de las estaciones. | -Datos estaciones | -Medias de las variables y desviaciones estándar | 63 |
| Arq | Recopila las arquitecturas seleccionadas con los errores más bajos. | -Resultados de las redes neuronales artificiales | -Número de neuronas seleccionadas en cada caso | 63 |
| Anydetest | Toma los errores más bajos de cada año de prueba, considerando las diferentes repeticiones y arquitecturas. | -Resultados de las redes neuronales | -Errores más bajos para cada año de prueba por estación | 63 |
| PMN-56 | Calcula los valores de $ET\_0$ a partir de la fórmula de PM-56. | -Datos estaciones\<br\>-Datos geográficos de las estaciones | -Valores diarios de $ET\_0$ | 63 |

-----

**Resumen de la metodología:**

Como resumen de la metodología seguida, el **Esquema de la Figura 13** ilustra los casos contemplados en el estudio. A partir de los datos de las estaciones, se evalúan los diferentes modelos neuronales y empíricos con los valores de $ET\_0$ calculados con el modelo de **Penman-Monteith** como referencia.
