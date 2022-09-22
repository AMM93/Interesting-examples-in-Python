# Author: Antonio Moreno Martín
# Example to understand how lists work on memory in Python

a = [1, 2, 3]
print("La lista 'a' creada es : " + str(b))

b = a
print("Por lo tanto, si apuntamos a 'a' a través de 'b', 'b' será igual que 'a': " + str(b))

# Ahora, añadimos a la lista a el número 4, por ende, 'a' irá del 1 al 4.
a.append(4)

# La pregunta ahora es, ¿a 'b' le ha ocurrido algo?
print(b)

# ¡Efectivamente! Como 'b' es una referencia a 'a', 'b' se ha visto mutado al modificar 'a'


# La nueva pregunta es, si modifico esta vez 'b', ¿'a' se verá afectado?
b.append(5)
print(a)

# ¡Por supuesto que también! ;)