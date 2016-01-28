# -*- coding: utf8 -*-

"""
   La lista en Python son variables que almacenan conjuntos de Datos (Array).
   Cada posicion de la lista es un elemento y estos elementos pueden tener
   diferentes tipos de datos.
   El primer elemento tendrá como posicion cero (0) y el ultimo elemento 
   tendrá como posicion la cantidad de elementos menos 1 (-1)
"""

# Ejemplo #1. Creacion de un list. En este list se puede observas que la creacion
#           se realiza con tipos de datos diferentes
l = [2, "tres", True, ["uno", 10]]
print "Ejemplo #1: " , l

# Ejemplo #2: Teniendo la lista creada "l", accedemos al dato que se encuentra
#             en la posicion 1 y creamos una variable "l2" a partir de "l"
#             con print l2, imprimimos lo que tiene en el momento la variable l2
l2 = l[1]
print "Ejemplo #2: " , l2

# Ejemplo #3: El elemento que se encuentra en la posicion 3 de la lista "l" es otra lista.
#             Para acceder a ella decimos:
l3 = l[3]
print "Ejemplo #3-1: " , l3

# Y para sacar uno de los elemetos de esa lista podemos decir:

lsub3 = l[3][0]
print "Ejemplo #3-2: " , lsub3

# o podemos...

lsub3 = l3[0]
print "Ejemplo #3-3: " , lsub3

# Ejemplo #4: Establecer nuevo valor a un elemento de la lista
#             A la posicion 1 de la lista le modificamos el valor
#             de "tres" a 4
l[1] = 4
print "Ejemplo #4: " , l

# Y la dejamos como estaba originalmente
l[1] = "tres"

# Ejemplo #5: Obtener un rango de elementos de la lista especifico

l5 = l[0:3]
print "Ejemplo #5: El valor final del rango 0 a 3 [0:3] no es agregado al resultado." , l5

# Ejemplo #6: Obtener un rango solamente con posiciones de elementos especificas
l6 = l[0:3:2]
print "lista: " , l , " código Ejecutado: l[0:3:2]" 
print "Resultado Ejemplo #6: " , l6

# Ejemplo #7: 

l7 = l[1::2]
print "Resultado Ejemplo #7: " , l7

