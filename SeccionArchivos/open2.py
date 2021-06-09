#!/usr/bin/env python
#_*_ coding: utf8 _*_

#r  = modo lectura

#metodo lee y hace split de datos en archivo. Split eliminara el \n. 
archivo = open('archivo1.txt','r')
for l in archivo.read().split():
    print(l)
