# Author: Antonio Moreno

def list_func(x):
    x[0] = 99
    
my_list = [1, 2, 3]
list_func(my_list)

# Antes de ejecutarlo, es interesante recordar que las listas son mutables, por tanto, el resultado debería ser [99, 2, 3]
print(my_list)

############################

# Sin embargo, los integers son INMUTABLES, por lo que el resultado para algunos no sea el esperado para este ejemplo tan sencillo


def int_func(x):
    x = x + 90
    
my_int = 3
int_func(my_list)

# Antes de ejecutarlo, es interesante recordar que las listas son mutables, por tanto, el resultado debería ser [99, 2, 3]
print("El resultado de la ejecución es: {}".format(my_int))

