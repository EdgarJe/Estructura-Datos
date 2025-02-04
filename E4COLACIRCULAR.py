class ColaCircular:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.cola = [None] * tamaño
        self.frente = 0
        self.final = 0
        self.vacia = True

    def esta_vacia(self):
        return self.vacia

    def esta_llena(self):
        return self.frente == self.final and not self.vacia

    def encolar(self, elemento):
        if self.esta_llena():
            print("La cola está llena. No se puede agregar el elemento.")
            return
        self.cola[self.final] = elemento
        self.final = (self.final + 1) % self.tamaño
        self.vacia = False

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía. No se puede desencolar un elemento.")
            return
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.tamaño
        if self.frente == self.final:
            self.vacia = True
        return elemento

    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return
        i = self.frente
        while i != self.final:
            print(self.cola[i], end=" ")
            i = (i + 1) % self.tamaño
        print()

# Ejemplo de uso
cola = ColaCircular(5)
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)
cola.mostrar()

cola.desencolar()
cola.mostrar()

cola.encolar(40)
cola.encolar(50)
cola.encolar(60)
cola.mostrar()
