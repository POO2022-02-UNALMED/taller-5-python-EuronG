from zooAnimales.animal import Animal


class Mamifero(Animal):
    _listado = None
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, self)
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

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
        #Mamifero.__init__(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
