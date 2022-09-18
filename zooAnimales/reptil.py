from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = None
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

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

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo):
        self._largoCola = largo

    def cantidadReptiles(self):
        return len(self.getListado())

    def crearIguanas(self, nombre, edad, genero):
        self.iguanas += 1
        self.__init__(nombre, edad, "humedal", genero, "verde", 3)

    def crearSerpientes(self, nombre, edad, genero):
        self.serpientes += 1
        self.__init__(nombre, edad, "jungla", genero, "blanco", 1)