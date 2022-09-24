import zooAnimales.animal as animal


class Ave(animal.Animal):
    _listado = None
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero, self)
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

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")