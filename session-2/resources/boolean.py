# -*- coding: utf8 -*-
import random

print '\nTipos de datos booleanos'
print '========================\n'

# Tipos de datos booleanos
aT = True
print "El valor es Verdadero:", aT, ", el cual es de tipo", type(aT), "\n"

aF = False
print "El valor es Falso:", aF, ", el cual es de tipo", type(aF)

print '\nOperadores booleanos'
print '====================\n'

# Operadores booleanos
aAnd = True and False
print "SI es Verdadero Y Falso, entonces es:", aAnd, ", el cual es de tipo", type(aAnd), "\n"

aOr = True or False
print "SI es Verdadero O Falso, entonces es:", aOr, ", el cual es de tipo", type(aOr), "\n"

aNot = not True
print "Si NO es Verdadero, entonces es:", aNot, ", el cual es de tipo", type(aNot), "\n"


print '\nUso Condicional'
print '====================\n'

aT = False
if aT:
   print "Es Verdadero, entonces aT es:", aT, "\n"
else:
   print "Es Falso, entonces aT cambio su valor y ahora es:", aT, "\n"


print '\nAhora otro ejemplo con un random una pareja elejirá'
print 'el nombre de su hijo dependiendo de si es un niño o no'
print '====================\n'

male = False
male = bool(random.randint(0, 1))

if (male):
   print "Es niño y le pondremos por nombre John"
else:
   print "Es niña y le pondremos por nombre Victoria"

print bool(dict())