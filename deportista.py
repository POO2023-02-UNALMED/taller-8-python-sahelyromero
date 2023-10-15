from .persona import Persona

class Deportista(Persona):

    def __init__(self, deporte, añosPracticando):

        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte
      
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAñosPracticando(self):
        return self._añosPracticando
      
    def setAñosPracticando(self, años):
        self._añosPracticando = años