print("logical_operators")
print(12 > 12 and 3 == 4)

print('Hola > Python: ',"Hola" > "Python")
print(3 > 4 and "Hola" > "Python")
print(3 == 3 or "Hola" > "Python")

# ejemplo

permiso_padres = True
mayor_edad = False

print('Debes de tener la mayoria de edad y permiso de tus padres para ir a la fiesta: ',(permiso_padres and mayor_edad))

tienes_licencia_conducir = True
tienes_carro=False
print('Para salir a conducir debes de tener licencia y carro: ',(tienes_licencia_conducir or tienes_carro))