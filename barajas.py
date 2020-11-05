from random import sample
from collections import Counter

PALOS = ['espada', 'corazón', 'rombo', 'trebol']
VALORES = ['as', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    baraja = []

    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo, valor))

    return baraja

def obtener_mano(baraja, tamano_mano):
    mano = sample(baraja, tamano_mano)
    
    return mano

def simular_manos(baraja, intentos, tamano_mano):
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)
    
    return manos

def par(valores_acumulados):
    """
    Regresa 1 si encuentra un par,
    de lo contrario regresa 0

    valores_acumulados es un arreglo con
    valores acumulados de la mano  
    """
    for val in valores_acumulados:
        if val == 2:
            return 1
    return 0

def doble_par(valores_acumulados):
    """
    Regresa 1 si encuentra dos pares,
    de lo contrario regresa 0

    valores_acumulados es un arreglo con
    valores acumulados de la mano  
    """
    contador = 0
    for val in valores_acumulados:
        if val == 2:
            contador += 1
    if contador == 2:
        return 1
    else:
        return 0

def triada(valores_acumulados):
    """
    Regresa 1 si encuentra una triada,
    de lo contrario regresa 0

    valores_acumulados es un arreglo con
    valores acumulados de la mano
    """
    for val in valores_acumulados:
        if val == 3:
            return 1
    return 0

def escalera(valores):
    """
    Regresa 1 si encuentra una escalera,
    de lo contrario regresa 0

    valores es un arreglo con todos los
    valores de la mano
    """
    valores_numericos = []
    for valor in valores:
        try:       # Funciona del 2 al 10
            valor_numerico = int(valor)
            valores_numericos.append(valor_numerico)

        except ValueError:  # Funciona con jota, reina, rey y as
            if valor == 'jota':
                valores_numericos.append(11)
            elif valor == 'reina':
                valores_numericos.append(12)
            elif valor == 'rey':
                valores_numericos.append(13)
            elif valor == 'as':
                valores_numericos.append(1)
                valores_numericos.append(14)
    
    valores_numericos.sort()    # ordenación acendente
    n_valores = len(valores_numericos)

    for i in range(n_valores - 1):  # ejemplo cuarta iteración [2, 3, 4, **5**, **6**]
        if valores_numericos[i] != valores_numericos[i + 1] - 1:
            if valores_numericos[i] != 1:   # escalera real [1, 10, 11, 12, 13, 14]
                return 0
        i += 1
    return 1

def color(palos):
    """
    Regresa 1 si encuentra un color,
    de lo contrario regresa 0

    palos es un arreglo con todos los
    palos de la mano
    """
    palo_carta_1 = palos[0] # Primer palo 
    for palo in palos:
        if palo_carta_1 != palo:
            return 0
    return 1

def full(valores_acumulados):
    """
    Regresa 1 si encuentra un full,
    de lo contrario regresa 0

    valores_acumulados es un arreglo con
    valores acumulados de la mano
    """
    un_par = par(valores_acumulados)
    una_triada = triada(valores_acumulados)
    if un_par == 1 and una_triada == 1: # ¿Hay par y triada?
        return 1
    else:
        return 0

def poker(valores_acumulados):
    """
    Regresa 1 si encuentra un poker,
    de lo contrario regresa 0

    valores_acumulados es un arreglo con
    valores acumulados de la mano
    """
    for val in valores_acumulados:
        if val == 4:
            return 1
    return 0

def escalera_de_color(valores, palos):
    """
    Regresa 1 si encuentra una escalera
    de color, de lo contrario regresa 0

    valores es un arreglo con todos los
    valores de la mano
    palos es un arreglo con todos los
    palos de la mano
    """
    una_escalera = escalera(valores)
    un_color = color(palos)
    if una_escalera == 1 and un_color == 1: # ¿Hay escalera y color?
        return 1
    else:
        return 0

def escalera_real_de_color(valores, palos):
    """
    Regresa 1 si encuentra una escalera
    real de color, de lo contrario regresa 0

    valores es un arreglo con todos los
    valores de la mano
    palos es un arreglo con todos los
    palos de la mano
    """
    una_escalera_de_color = escalera_de_color(valores, palos)

    if una_escalera_de_color == 1:              # ¿Hay escalera de color?
        if '10' in valores and 'as' in valores: # ¿Cohexisten el 10 y el as?
            return 1
        else:
            return 0
    return 0

def main(tamano_mano, intentos):
    baraja = crear_baraja()
    jugadas = {
        'par': 0, 
        'doble par': 0, 
        'triada': 0, 
        'escalera': 0, 
        'color': 0, 
        'full': 0,
        'poker': 0,
        'escalera de color': 0,
        'escalera real de color': 0 
        }
    
    manos = simular_manos(baraja, intentos, tamano_mano)
    
    for mano in manos: # Obtiene palos y valores
        valores = []
        palos = []
        for carta in mano:
            valores.append(carta[1])
            palos.append(carta[0])

        counter = dict(Counter(valores))
        
        jugadas['par'] += par(counter.values())
        jugadas['doble par'] += doble_par(counter.values())
        jugadas['triada'] += triada(counter.values())
        jugadas['escalera'] += escalera(valores)
        jugadas['color'] += color(palos)
        jugadas['full'] += full(counter.values())
        jugadas['poker'] += poker(counter.values())
        jugadas['escalera de color'] += escalera_de_color(valores, palos)
        jugadas['escalera real de color'] += escalera_real_de_color(valores, palos)

    for jugada in jugadas.keys():   # Imprime y calcula resultados
        probabilidad = jugadas[jugada] / intentos
        print(f'la probabilidad de sacar {jugada} en una mano de {tamano_mano} es de {probabilidad}')

    
if __name__ == '__main__':

    tamano_mano = int(input('ingrese el tamaño de la mano: '))
    intentos = int(input('ingrese el número de intentos: '))

    main(tamano_mano, intentos)