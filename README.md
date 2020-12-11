# Probabilidades de cada mano del poker
Por medio de la simulación se estima la probabilidad de todas las manos del poker.

El tamaño de la mano es la cantidad de cartas por mano (5 es lo común). El número de intentos es la cantidad de veces que la simulación se ejecutará; este será pedido al ejecutar el programa. Mientras más alto, más precisa la estimación.

#### Ejemplo:

Al ejecutarse, primero te pedirá el tamaño de la mano.
`ingrese el tamaño de la mano: 5`  

Después la cantidad de intentos:
`ingrese el número de intentos: 10000000`

**Output:**
```
la probabilidad de sacar par en una mano de 5 es de 0.4448248
la probabilidad de sacar doble par en una mano de 5 es de 0.0411573
la probabilidad de sacar triada en una mano de 5 es de 0.0193994
la probabilidad de sacar escalera en una mano de 5 es de 0.0064548
la probabilidad de sacar color en una mano de 5 es de 0.0020706
la probabilidad de sacar full en una mano de 5 es de 0.0011263
la probabilidad de sacar poker en una mano de 5 es de 0.0001875
la probabilidad de sacar escalera de color en una mano de 5 es de 2.13e-05
la probabilidad de sacar escalera real de color en una mano de 5 es de 1.5e-06
```

**NOTA:** *Es recomendable que el número de intentos de la simulación sea mayor o igual a 10 millones*
