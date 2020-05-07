# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:38:36 2020

@author: elber
"""
a = 1
b = "texto"
c = 0.03
d = False
dicionario = {"teste": "dicionario"}
lista = [a,b,c,d,dicionario]
tupla = ("teste tupla", lista)

print(type(tupla))

for x in tupla:
    if type(x) == list:
        for y in x:
            print(type (y))
    else:
        print(type (x))