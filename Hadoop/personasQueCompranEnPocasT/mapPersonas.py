#!/usr/bin/python
import sys


#Por cada medida de temp emitimos los pares <nombre,valor>
for compras in sys.stdin:
    compras = compras.strip()
    nombre , tienda = compras.split()    

    print("%s\t%s"%(nombre,tienda))
    
