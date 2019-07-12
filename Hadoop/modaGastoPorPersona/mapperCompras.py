#!/usr/bin/python
import sys


#Por cada medida de temp emitimos los pares <nombre,valor>
for compras in sys.stdin:
    compras = compras.strip()

    nombre = compras.split()
    

    print( "%s\t%s"%( nombre,1))
    
