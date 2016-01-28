# multiple return is actualy a tuple
def first_multiples(num):
	return num, num * 2, num * 3, num * 4


def sum(*vars):
	total = 0
	for i in vars:
		total+= i
	return total

#unpacking example
a, b, c, d = first_multiples(2)

print a,b,c,d



#procedure return as tuple

ret = first_multiples(3)

print ret

#accessing tuple positions with []
print ret[0]
print ret[1]
print ret[2]
print ret[3]


#tuples are inmmutable

#ret[0] = 0 # this line should throw an error


#tuple concatenation (generates a diferent tuple since they are inmuables)
print ret + ret

#packing parameters as tuples
print sum(1,2,3,4,5,6,7,8)

print sum(*(first_multiples(3) + first_multiples(4)))
