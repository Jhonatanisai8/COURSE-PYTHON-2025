print("01_access_lists.py".upper())

my_list = list(["Tierra","Venus",12,True,7.5])
print(my_list)

my_list.append(12)
print(my_list)

# elimina el primer elemento que encuentra
my_list.remove(12)
print(my_list)

# elimina por indice 
my_list.pop(1)
print(my_list)
my_pop_element = my_list.pop(3)
print(my_pop_element)
print(my_list)

# inserta por indice
my_list.insert(0,"primero")
print(my_list)

# copiamos una lista 
my_list_copy = my_list.copy()
print(my_list_copy)

my_list.clear()
print(my_list)

my_list_copy.reverse()
print(my_list_copy)