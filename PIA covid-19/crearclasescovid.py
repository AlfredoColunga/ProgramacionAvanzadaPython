def main():
  class pais():
    # Se asignan atributos a la clase "pais"
    def __init__(self, nombreIng, nombreEsp, poblacion, fallecidos, pdc, contagiados):
      self.nombreIng = nombreIng
      self.nombreEsp = nombreEsp
      self.poblacion = poblacion
      self.fallecidos = fallecidos
      self.pdc = pdc
      self.contagiados = contagiados
  class incidente():
    # Se asignan atributos a la clase "incidente"
    def __init__(self, pais, fecha, numContagios, numFallecidos):
      self.pais = pais
      self.fecha = fecha
      self.numContagios = numContagios
      self.numFallecidos = numFallecidos