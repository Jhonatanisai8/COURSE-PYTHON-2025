print("formatting")
mi_name,mi_lastname ,age= "Isai","Ojeda",19
print("Mi nombre es Isai")
# formateamos
print("Mi nombres es {} , mi apellido es {} y tengo {} años".format(mi_name,mi_lastname,age))

print("Mi nombres es %s , mi apellido es %s y tengo %s años" %(mi_name,mi_lastname,age))

print("Mi nombre es "+mi_name+" y mi apellido "+mi_lastname+", tengo "+str(age))
# formatos con numeros #
print("Mi nombres es %s , mi apellido es %s y tengo %d años" %(mi_name,mi_lastname,age))

# inferencia de datos
print(f"Mi nombres es {mi_name} , mi apellido es {mi_lastname} y tengo {age} años")
