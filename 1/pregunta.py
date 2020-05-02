# Se preguntan datos y se validan con expresiones regulares

# Módulo  para expresiones regulares
import re

# Módulo para datos datetime
import datetime

# Se declara una variable de paso para capturar datos
_captura=""

# Función para validar los datos
def pregunta(_formato,_pregunta="Datos: "):
    # Se especifica que "_captura" es global
    global _captura
    while True:
      _dato = input(_pregunta)
      valido = re.search(_formato,_dato)
      if (valido):
        _captura = _dato
        break
      else:
        print("Dato invalido")

# Función para convertir cadena a datetime
def cadenafecha(_dtDato):
    return datetime.datetime(int(_dtDato[0:4]), int(_dtDato[5:7]), int(_dtDato[-2:]))

def main():
    # Se pregunta ID de 4 dígitos
    pregunta("^[0-9]{4}$","Ingrese ID (4 dígitos): ")
    ident = _captura
    # Se pregunta un nombre en mayusculas, de 1 a 30 dígitos con espacios
    pregunta("^[A-Z ]{1,30}$","Ingrese nombre en mayusculas: ")
    nombre = _captura
    # Se pregunta Si o No (S/N)
    pregunta("^[S|N]$","Acepta (S/N): ")
    acepta = _captura  
    # Se pregunta una fecha
    pregunta("^[0-9]{4}-[0-9]{2}-[0-9]{2}", "Ingrese fecha (YYYY-MM-DD): ")
    fecha = _captura

    print(ident)
    print(nombre)
    print(acepta)
    print(fecha)