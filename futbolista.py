from persona import Persona
from deportista import Deportista

class Futbolista(Deportista, Persona):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):

        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)

        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, value):
        self._golesMarcados = value

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, value):
        self._tarjetasRojas = value

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, value):
        self._piernaHabil = value

    def getListaFutbolistas(cls):
        return Futbolista.listaFutbolistas
    
    def setListaFutbolistas(cls, value):
        Futbolista.listaFutbolistas = value

    def __str__(self):

        return (f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {str(self.getEdad)} años de edad y llevo {str(self.getAñosPracticando)} años en el deporte")