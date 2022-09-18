from zooAnimales.animal import Animal


class Pez(Animal):
    _listado = None
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

        if self._listado is None:
            self._listado = [self]
        else:
            self._listado.append(self)

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    def cantidadPeces(self):
        return len(self.getListado())

    def crearSalmon(self, nombre, edad, genero):
        self.salmones += 1
        self.__init__(nombre, edad, "oceano", genero, "rojo", 6)

    def crearBacalao(self, nombre, edad, genero):
        self.bacalaos += 1
        self.__init__(nombre, edad, "oceano", genero, "gris", 6)