from node import Node

# Nodos
a = Node(11)
b = Node(3)
c = Node(14)
d = Node(102)
e = Node(48)

# Enlazado
a.next = b
b.next = c
c.next = d
d.next = e

# Punteros de la lista
head = a
tail = e

# Recorrido
# Visitar el primer nodo
current = head
print('Primer nodo', current.data)

# Visitar el segundo nodo
current = current.next
print('Segundo nodo', current.data)

# Visitar el tercer nodo
current = current.next
print('Tercer nodo', current.data)

# Visitar el cuarto nodo
current = current.next
print('Cuarto nodo', current.data)

# Visitar el quinto nodo
current = current.next
print('Quinto nodo', current.data)

if current.next is None:
    print('Ya visitó todos los nodos')
else:
    print('Faltan nodos por visitar')


