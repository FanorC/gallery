#!/usr/bin/python
import sys

'''
Created on Nov 24, 2018

@author: fanor.camacho
'''


nombreActual=None
totalGastado=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    nombre, valor = claveValor.split("\t")

    valor= int(valor)
    
    if nombreActual==None:
        nomnbreActual=nombre
        


    if nombreActual==nombre:
        totalGastado+=valor
    else:
        if nombreActual:
            print("%s\t%s"%(nombreActual,totalGastado))
        nombreActual=nombre
        totalGastado=valor
        
if nombreActual==nombre:
    print("%s\t%s"%(nombreActual,totalGastado))