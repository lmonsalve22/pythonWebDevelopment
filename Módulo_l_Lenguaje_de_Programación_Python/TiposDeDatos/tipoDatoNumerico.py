# -*-coding:utf-8 -*-
#######################
#Tipo de dato numérico#
#######################
"""Comentario de varias líneas"""

miNumero = 123
a = 10
b = -3
c = 3.14
d = 10j

print("Tipo de dato de a: ",type(a))
print("Tipo de dato de b: ",type(b))
print("Tipo de dato de c: ",type(c))
print("Tipo de dato de d: ",type(d))

print("a+b",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a%2",a%2)
print("a+d",a+d)
print("j*j",1j*1j)

#El tamaño máximo de un entero es : 2^63-1 o 2^31-1 dependiendo de la arquitectura del S.O
"""
>>> import sys
>>> a=sys.maxsize
>>> print type(a)
  File "<stdin>", line 1
    print type(a)
             ^
SyntaxError: invalid syntax
>>> print(type(a))
<class 'int'>
>>> a+=1
>>> print(type(a))
<class 'int'>
>>> sys.maxsize
9223372036854775807
"""
#Manejo de  bases

octal = 0o122
hexadecimal = 0x9ff
binario = 0b1111

print("Octal %o = Decimal %d"%(octal,octal))
print("Hexadecimal %x = Decimal %d"%(hexadecimal,hexadecimal))
print("Binario", bin(binario), "Decimal %d "%binario)


