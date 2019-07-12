#!/usr/bin/python


valorActual=0
nombreActual=None
tiendaActual=None
contador=0
contadorActual=0

for claveValor in sys.stdin:
    claveValor= claveValor.strip()
    
    nombre, tienda = claveValor.split()
     



  
# # # moda                                                                                   
    if nombreActual==None:
        nombreActual=nombre
        tiendaActual=tienda
        

          
          
        

#primer nombre, alicia
    if nombreActual==nombre:
        if tiendaActual==tienda :  
            contador=1
        if tiendaActual!=tienda :         
                contador=contador+1
            
    
            

    else:
        if contador<=3:          
            print("%s"%(nombreActual))
        nombreActual=nombre
        tiendaActual=tienda
        contador=1
       
        
#
if contador<=3:         
    print("%s"%(nombreActual))    
