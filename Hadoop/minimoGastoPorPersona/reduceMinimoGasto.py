#!/usr/bin/python
import sys

'''
Created on Nov 24, 2018

@author: fanor.camacho
'''


nombreActual=None
valorMinimo=None
compraAlta=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    nombre, valor = claveValor.split("\t")

    valor= int(valor)
    
    if nombreActual==None:
        nombreActual=nombre
        valorMinimo=valor
        


    if nombreActual==nombre:
        if valor<valorMinimo:
            valorMinimo=valor
    else:
        
        print("%s\t%s"%(nombreActual,valorMinimo))
        nombreActual=nombre
        valorMinimo=valor
        
        
        
        
        

print("%s\t%s"%(nombreActual,valorMinimo))