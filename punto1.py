# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:50:32 2022

@author: jariza36
"""

valordonado = int(input("valor total"))
valortele = valordonado*0.1
valosiste = valordonado*0.25
valoradmi = valordonado*0.35
vcontabilidad = valortele - valosiste - valoradmi

print(f'El valor del donado es de: ${valortele:,}')
print(f'El valor del  donad  es de: ${valosiste:,}')
print(f'El valor del  donad es de: ${valoradmi:,}')

#java