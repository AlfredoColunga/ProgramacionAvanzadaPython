# Se preguntan datos y se validan con expresiones regulares
# Módulo  para expresiones regulares
import re
# Módulo para datos datetime
import datetime
# Se declara una variable de paso para capturar datos
_captura=""
def pregunta(_formato,_pregunta="Dato: "):
    pass
def main():
    #Se pregunta ID de 4 dígitos
    pregunta("^[0-9]{4}$","Ingrese ID (4 dígitos: ")
    id = _captura
    #Se pregunta un nombre en mayusculas, de 1 a 30 dígitos con espacios
    pregunta("^[A-Z ]{1,30}$","Ingrese nombre en mayusculas: ")
    nombre = _captura
    #Se pregunta Si o No (S/N)
    pregunta("^[S|N]$","Acepta (S/N): ")
    fecha = _captura
    #Se pregunta una fecha
    pregunta("^[0-9]{4}")