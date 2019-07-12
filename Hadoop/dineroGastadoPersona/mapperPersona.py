#!/usr/bin/python
import sys


#Por cada medida de temp emitimos los pares <nombre,valor>
for compras in sys.stdin:
    compras = compras.strip()
    nombre , valor = compras.split()    

    print("%s\t%s"%(nombre,valor))
    