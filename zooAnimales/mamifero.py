from zooAnimales.animal import Animal


class Mamifero(Animal):
    _listado = None
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super.__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

        if self._listado is None:
            self._listado = [self]
        else:
            self._listado.append(self)

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    def isPelaje(self):
        return self._pelaje

    def cantidadMamiferos(self):
        return len(self.getListado())

    def crearCaballo(self, nombre, edad, genero):
        self.caballos += 1
        self.__init__(nombre, edad, "pradera", genero, True, 4)

    def crearLeon(self, nombre, edad, genero):
        self.leones += 1
        self.__init__(nombre, edad, "selva", genero, True, 4)
