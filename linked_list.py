from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traversal(self) -> str:
        pass

    def search(self, data) -> Node:
        pass

    def prepend(self, data) -> Node:
        pass

    def append(self, data) -> Node:
        pass

    def remove(self, data) -> Node:
        pass

    from node import Node

    def esta_vacia(self):
        return self.head == None and self.tail == None

    def insertar_inicio(self, nombre):
        nuevo = Node(nombre)
        if self.esta_vacia():
            self.head = nuevo
            self.tail = nuevo
        else:
            aux = self.head
            self.head = nuevo
            nuevo.next = aux
        self.size += 1

    def recorrer(self):
        resultado = ''
        aux = self.head
        while aux != None:
            if aux == self.tail:
                resultado += str(aux)
            else:
                resultado += str(aux) + ' -> '
            aux = aux.next

        return resultado
