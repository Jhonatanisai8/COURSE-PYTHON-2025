"""
Escribir un programa que almacene en una lista los siguientes
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el 
menor y el mayor de los precios.
"""

mi_lista = [50, 75, 46, 22, 80, 90, 8]
elemento_mayor = mi_lista[0]
elemento_menor = mi_lista[0]
for i in range (len(mi_lista)):
    if elemento_mayor < mi_lista[i]:
        elemento_mayor = mi_lista[i]
    if elemento_menor > mi_lista[i]:
        elemento_menor = mi_lista[i]
    
        
print(elemento_mayor)
print(elemento_menor)