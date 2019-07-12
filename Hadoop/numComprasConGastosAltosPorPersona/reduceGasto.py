#!/usr/bin/python
import sys

'''
Created on Nov 24, 2018

@author: fanor.camacho
'''


nombreActual=None
valorActual=None
compraAlta=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    nombre, valor = claveValor.split("\t")

    valor= int(valor)
    
    if nombreActual==None:
        nombreActual=nombre
        


    if nombreActual==nombre:
        if valor>3000:
            compraAlta=compraAlta+1
    else:
        
        print("%s\t%s"%(nombreActual,compraAlta))
        nombreActual=nombre
        valorActual=valor
        if valorActual>3000:
            compraAlta=1
        else:
            compraAlta=0
        
        
        
        

print("%s\t%s"%(nombreActual,compraAlta))