print("Access Lists")

my_lists = list({11,12,23})

print(my_lists[1]) #11
print(type(my_lists))

print(my_lists[-3])

# tamaño de la lista
print(len(my_lists))

# contamos un elemento
print(my_lists.count(11))

list1 = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1.count("apple"))
print(thislist[1:3])

# desempaquetado
my_list_isa = [19,1.81,"Jhonatan"]
age, height,name = my_list_isa
print(age)

my_list_isa = [19,1.81,"Jhonatan"]
age, height,name = my_list_isa[1] ,my_list_isa[1],my_list_isa[1]
print(height)
print(name)

list_01 = ["Hola",12,True,34.3]
list_02 = ["Mundo",True,11,34.3]
print(type(list_01))

# cancatenacion de listas
print(f"Resultado de: ",type(list_01 + list_02))
print(list_01 + list_02)

list_01 = "Lista"
print(list_01)
print(type(list_01))