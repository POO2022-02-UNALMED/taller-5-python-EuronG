from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = None
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPlumas = color

        if self._listado is None:
            self._listado = [self]
        else:
            self._listado.append(self)

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, plumas):
        self._colorPlumas = plumas

    def cantidadAves(self):
        return len(self.getListado())

    def crearHalcon(self, nombre, edad, genero):
        self.halcones += 1
        self.__init__(nombre, edad, "montanas", genero, "cafe glorioso")

    def crearAguila(self, nombre, edad, genero):
        self.aguilas += 1
        self.__init__(nombre, edad, "montanas", genero, "blanco y amarillo")