
# Inteligencia Artificial
> CC421 - Prática Calificada N° 2

<img src="taxi.png" align="center" />

## Equipo 1
   - [Jesús Andrés Torrejón León](https://github.com/JesusATL)
   - [Jordi Joel Bardales Rojas](https://github.com/jbardalesr)
   - [Walter Jesús Felipe Tolentino](https://github.com/felipeturing)
   - [Julio César Yaranga Santé](https://github.com/cesar-yaranga)

## Cuadernos de revisión

    - **Red Neuronal de Capas Densas con 25M** : [FullyConnectedNNTorch.ipynb](https://github.com/felipeturing/pc2-team1-ai/blob/main/SubNotebook1/FullyConnectedNNTorch.ipynb)
    - **GradientBoostingRegressor    con 55M** : [RFyGradBoost DatosCompletos.ipynb](https://github.com/felipeturing/pc2-team1-ai/blob/main/SubNotebook1/RFyGradBoost%20%20DatosCompletos.ipynb)
    - **Random Forest Regressor      con 55M** : [RFyGradBoost DatosCompletos.ipynb](https://github.com/felipeturing/pc2-team1-ai/blob/main/SubNotebook1/RFyGradBoost%20%20DatosCompletos.ipynb)
    - **Regresión Lineal             con 1M**  : [Pruebas.ipynb](https://github.com/felipeturing/pc2-team1-ai/blob/main/SubNotebook1/Pruebas.ipynb)

## Objetivo

El objetivo de esta evaluación es construir un modelo de aprendizaje que sea capaz de
predecir la tarifa que cobra un taxi de acuerdo a cierta información de entrada.

## Resumen

Se ha obtenido una muestra representativa de 25M de registros con PySpark (en algunas pruebas se logró trabajar con todos los datos), luego se desarrolló la **limpieza** con buen críterio (analizando con gráficos y consultas) determinando los dominios de validación de la cantidad de pasajeros, tarifa y región geográfica (este último inicialmente de forma general), para posteriormente limpiar aquellos registros fuera de los dominios. La implementación de la limpieza general se encuentra en el método filter_data(.).

Con un análisis análogo al anterior se desarrolló la **transformación** de puntos de una región geográfica (no íncluida en la región validada) a la región validada, entendiendo que los registros fuera la región en realidad tenían las coordenadas intercambiadas. La implementación de esta transformación se encuentra en el método swap_coordinates(.), luego como los datos ya se transformaron, se limpia los puntos fuera la región geográfica de New York (deducida de graficar los puntos en un mapa).

Antes de desarrollar la **Ingeniería de Características**, se **explora** algún patrón que relacione la variabilidad de la tarifa con ciertas regiones de New York, encontrando que en los tres aeropuertos de New York, los cuales son John F. Kennedy Airport (JFK), LaGuardia (LGA) y Newark Airport (EWR), las tarifas son elevadas respecto al resto de regiones, luego verificando este resultado con las tarifas estandares de La Comisión de Taxis y Limusinas de la Ciudad de Nueva York (TLC), se comprueba que lo encontrado corresponde con la realidad, revisar https://www1.nyc.gov/site/tlc/passengers/taxi-fare.page, para el detalles de tarifas. Por lo tanto se considera la características *pickup_airport* y *dropoff_airport* para saber si el taxi sale o llega en algún aeropuerto.

Una característica evidente es considerar la distancia entre los puntos de partida y llegada, para esto se determina la distancia de Haversine que permite encontrar la distancia entre dos puntos dado la latitud y longitud de los puntos, dicha característica se llama *distance*.

Asímismo analizando la columna datetime se encontró cierta dependencia entre la tarifa y el año, mes, hora y día de la semana, por eso se crean las características *year*, *month*, *day*, *hour*, *weekday*.

Finalmente se ha *evaluado ciertos modelos* para determinar el que mejor se acomode a nuestros datos y métricas esperadas (RMSE y R2SCORE), los modelos que hemos probado son: Regresión Lineal, Regresión Polinómica, RandomForestRegressor, GradientBoostingRegressor y Red Neuronal de Capas Densas.


# Resultados

    - **Red Neuronal de Capas Densas** con 25M : RMSE 3.5575 y R2SCORE 0.8335.
    - **GradientBoostingRegressor**    con 55M : RMSE 3.5441 y R2 0.8350.
    - **Random Forest Regressor**      con 55M : RMSE 3.8728 y R2 0.8030.
    - **Regresión Lineal**             con 1M  : RMSE 3.8077 y R2 0.8088.

## Interpretación de Resultados

Como tenemos aprox 3.5 de RMSE en los mejores casos significa que podemos esperar que el modelo no se equivoque en mas de 3 unidades en la tarifa predecida.

## Contribuir

Las contribuciones son siempre bienvenidas

## Licencia

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
