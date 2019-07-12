#!/usr/bin/python
import sys


valorEstimado=0
valorGastado=0
nombreActual=None


error=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    nombre, valor = claveValor.split('\t',1)

    valor= int(valor)
    
    if nombreActual==None:
        nombreActual=nombre
        valorGastado=valor
        

        

    if nombreActual==nombre: 
         
                
        if valorGastado==valor:
            valorGastado
        else:
            valorEstimado=valor
        

        error=valorEstimado-valorGastado
    
       

    else:
       
        print("%s\t%s"%(nombreActual,error))

        nombreActual=nombre
        valorGastado=valor
                                                             
        
print("%s\t%s"%(nombre,error))