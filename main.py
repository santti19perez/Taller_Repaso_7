from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Elemento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.__elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elemento == e for e in self.__elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.__elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.__elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [e for e in conjunto1.__elementos if conjunto2.contiene(e)]
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_interseccion)
        for elemento in elementos_interseccion:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.__elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


# Aca decidi añadir un ejemplo de como todoo esto va a funcionar:
if __name__ == "__main__":
    elemento1 = Elemento("A")
    elemento2 = Elemento("B")
    elemento3 = Elemento("C")
    elemento4 = Elemento("B")

    conjunto1 = Conjunto("Conjunto1")
    conjunto1.agregar_elemento(elemento1)
    conjunto1.agregar_elemento(elemento2)
    conjunto1.agregar_elemento(elemento4)

    conjunto2 = Conjunto("Conjunto2")
    conjunto2.agregar_elemento(elemento2)
    conjunto2.agregar_elemento(elemento3)

    conjunto3 = conjunto1 + conjunto2
    print(conjunto3)

    conjunto4 = Conjunto.intersectar(conjunto1, conjunto2)
    print(conjunto4)
