#! /usr/bin/env python

#instanciar un diccionario
def definition():
    myDictionary = {'jack': 4098, 'sape': 4139}
    print myDictionary

#instanciar un diccionario 2
def definition2():
    myDictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print myDictionary

#instanciar un diccionario 3
def definition3():
    myDictionary = {x: x**2 for x in (2, 4, 6)}
    print myDictionary

#instanciar un diccionario y validar igualdad
def definition4():
	a = dict(one=1, two=2, three=3)
	b = {'one': 1, 'two': 2, 'three': 3}
	c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
	d = dict([('two', 2), ('one', 1), ('three', 3)])
	e = dict({'three': 3, 'one': 1, 'two': 2})
	print a == b == c == d == e

#agregar un elemento a un diccionario
def addElement():
    myDictionary = {'jack': 4098, 'sape': 4139}
    print myDictionary
    print 'add element'
    myDictionary['guido'] = 4127
    print myDictionary

#Actualizar un elemento ya existente
def updateElement():
    myDictionary = {'jack': 4098, 'sape': 4139}
    print myDictionary
    print 'update element'
    myDictionary['jack'] = 4127
    print myDictionary

#eliminar un elemento
def deleteElement():
    myDictionary = {'jack': 4098, 'sape': 4139}
    print myDictionary
    print 'update element'
    del myDictionary['sape']
    print myDictionary

#obtener las llaves de un diccionario
def getKeys():
    myDictionary = {'jack': 4098, 'sape': 4139}
    print myDictionary
    print 'dictionary keys'
    print myDictionary.keys()

#validar si existe una llave en un diccionario
def existsElement():
	myDictionary = {'jack': 4098, 'sape': 4139}
	print myDictionary
	print 'guido does not exists',('guido' not in myDictionary)
	print 'jack exists',('jack' in myDictionary)

#definir cantidad de elementos en un diccionario
def countElements():
	myDictionary = {'jack': 4098, 'sape': 4139}
	print myDictionary
	print len(myDictionary)

#listar elementos como una tupla
def items():
	dict = {'Name': 'Zara', 'Age': 7}
	print "Value : %s" %  dict.items()

#
def iterateElements(): 
	knights = {'Mance Rayder': 'King-Beyond-the-Wall', 'Khaleesi': 'Mother of Dragons', 'Gregor Clegane':'The Mountain That Rides'}
	for k, v in knights.iteritems():
		print k, 'AKA' ,v