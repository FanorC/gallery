#!/usr/bin/python
import sys


for compras in sys.stdin:
    compras = compras.strip()
    persona, tipo , valor = compras.split('\t', 2) 
    print("%s\t%s"%( persona , valor ))

