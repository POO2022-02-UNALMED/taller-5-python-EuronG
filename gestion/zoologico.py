class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._zonas = None
        self._nombre = nombre
        self._ubicacion = ubicacion

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas

    def setZonas(self, zonas):
        self._zonas = zonas


    def agregarzonas(self, zona):
        if self._zonas is None:
            self._zonas = [zona]
        else:
            self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        r = 0
        for i in self.getZonas():
            r += i.cantidadAnimales()
        return r