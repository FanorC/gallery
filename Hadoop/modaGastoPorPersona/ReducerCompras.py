#!/usr/bin/python
import sys

'''
Created on Nov 24, 2018

@author: fanor.camacho
'''


valorActual=0
nombreActual=None
contador=0
contadorActual=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    nombre,   apariciones = claveValor.split("\t")

    apariciones= int(apariciones)

  
# # # moda                                                                                   
    if nombreActual==None:
        nombreActual=nombre

          
          
        

#primer nombre, alicia
    if nombreActual==nombre:
         
        contador=contador+apariciones
        if apariciones>contador:
            contador=apariciones  

    else:
        if contador>apariciones:                
            print("%s\t%s"%(nombreActual,contador))
        nombreActual=nombre
        contador=apariciones
        
print("%s\t%s"%(nombreActual,contador))    
'''
Obtenemos que el valor alicia 120 se repite 4 veces y Bob 50 se 3'''
