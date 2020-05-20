__author__ = "Sebastián Stiven Ramirez David"
__copyright__ = "Copyright 2020, Random Number Draw Game, University Project"
__credits__ = "juanpabloaj --> moda_media.py "
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "sebas551v@gmail.com"
__status__ = "Production"

import random   #librería para generar números aleatorios

numPropuesto = 0    #variable int para almacenar el número que el usuario indica
enJuego = True      #variable booleana que se usa como bandera para indicar que el juego está activo, si cambia a false el juego termina
numTotales = []      #vector que almacena el total de los números propuestos por todos los participantes
contParticipante = 1     #contador que indica el número de participantes  
numIntentos = int(input("Ingrese el número de intentos permitidos por participante: "))   #variable int para almacenar el número de intentos que tendrá cada participante

while enJuego:       #ciclo mientras. Está activo mientras la bandera sea verdadera         
    numGanador = random.randint(1, 99)  #variable número ganador. randint --> genera un número aleatorio entre 1 y 99
    print(f"PARTICIPANTE {contParticipante}")
    intento = 0     #indica el intento en el que se encuentra cada jugador
    numerosParticipante = []   #vector que almacena los números propuestos por cada participante    
    for intento in range(numIntentos):        
        numPropuesto = int(input("Ingrese un número entre 1 y 99: "))   #Solicita un número al usuario. El número llega como un String por lo que hay que hacerle un cast a int 
        intento += 1        #incrementa el intento
        numerosParticipante.append(numPropuesto)      #Se almacena el número ingresado en el vector de números propuestos
        numTotales.append(numPropuesto)
        if (numPropuesto > numGanador):                  #Validación para números mayores al ganador
            print("El número ingresado es mayor que el número ganador")
        if (numPropuesto < numGanador):                  #Validación para números mayores al ganador
            print("El número ingresado es menor que el número ganador")
        if (numPropuesto == numGanador):                  #Validación para números mayores al ganador
            print("El número ingresado es el número ganador!!!")
            enJuego = False
            break
        if(intento >= numIntentos):       #valida que el intento actual no sea superior al número de intentos permitidos por participante
            print("Agotó el número de intentos")       
            enJuego = False
    
    numMayor = numerosParticipante[0]        #Variable que almacena el mayor número propuesto por el participante. Su valor inicial es el primero número propuesto por el participante
    numMenor = numerosParticipante[0]        #Variable que almacena el menor número propuesto por el participante. Su valor inicial es el primero número propuesto por el participante
    contMayores = 0     #Contador para los números mayores al número ganador
    contMenores = 0     #Contador para los números menores al número ganador
    numeros = []        #Vector para almacenar los números propuestos por el participante
    mayores = []        #Vector para almacenar los números propuestos por el participante que están por encima del número ganador
    menores = []        #Vector para almacenar los números propuestos por el participante que están por debajo del número ganador
    for element in numerosParticipante:         #ciclo para recorrer los números propuestos por cada participante adenas de los números mayores y los números menores al número ganador
        numeros.append(element)
        if (element > numGanador):
            mayores.append(element)
            contMayores += 1
        if (element < numGanador):
            menores.append(element)
            contMenores +=1
        if (element > numMayor):
            numMayor = element        
        if (element < numMenor):
            numMenor = element
    
    print(f"Cantidad de intentos del participante {contParticipante}: {intento}")    
    print(f"Números propuestos por el participante {contParticipante}: ",numeros)
    print(f"Mayor número propuesto por el participante {contParticipante}:  {numMayor}")
    print(f"Menor número propuesto por el participante {contParticipante}:  {numMenor}")
    print(f"Números por debajo del número ganador propuestos por el participante {contParticipante}: ", menores)
    print(f"Cantidad de números por debajo del número ganador propuestos por el participante {contParticipante}:  {contMenores}")
    print(f"Números por encima del número ganador propuestos por el participante {contParticipante}: ", mayores)
    print(f"Cantidad de números por encima del número ganador propuestos por el participante {contParticipante}:  {contMayores}")
    if(not enJuego):
        nuevoParticipante = int(input("¿Nuevo participante?  Sí --> 1  ,  No --> 2:  "))

        if(nuevoParticipante == 1):
            enJuego = True
            contParticipante += 1

repeticiones = 0            #Variable que almacena la cantidad de veces que se repiten los números moda dentro de todos los propuestos por los participantes          
for element in numTotales:      #Ciclo para encontrar la cantidad mayor en la que se repite un número entre los propuestos por los participantes
    apariciones = numTotales.count(element)
    if apariciones > repeticiones:
        repeticiones = apariciones
modas = []          #Vector que almacena los números que más se repiten entre los propuestos por todos los participantes
for element in numTotales:      #Ciclo para encontrar los números que se repiten la cantidad de veces hallada en el ciclo anterior dentro de los números propuestos por los participantes
    apariciones = numTotales.count(element)
    if apariciones == repeticiones and element not in modas:
        modas.append(element)

print(f"El total de participantes fue: {contParticipante}")
print("El número o los números que más veces fueron propuestos entre todos los participantes: ", modas)
print("GAME OVER")
