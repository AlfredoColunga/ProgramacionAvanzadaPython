# Se importa el módulo (datetime) para mostrar datos de tipo datetime
import datetime
# Notación húngara:
# str - string
# i - int
# f - float
# dt - date

def main():
 print("==CAPTURA DE DATOS==") 
 # Si el dato es string solo necesita una variable
 strDato = input("Ingrese dato de tipo string: ")
 # Si el dato es de tipo int se usa una variable de paso (_iDato) que es string
 _iDato = input("Ingrese dato de tipo integer: ")
 # La variable (iDato) almacena en int el dato capturado en la variable de paso
 iDato = int(_iDato)
 # Si el dato es de tipo float se usa una variable de paso (_fDato) que es string
 _fDato = input("Ingrese dato de tipo float: ")
 # La variable (fDato) almacena en float el dato capturado en la variable de paso
 fDato =float(_fDato)
 # Si el dato es de tipo date se usa una variable de paso (_dtDato) que es string
 _dtDato = input("Ingrese una fecha (YYYY/MM/DD): ")
 # [n,m] Extrae desde la posición "n" a la posición "m" (sin incluir "m")
 # [-m:] Extrae desde la posición "m", de atrás hacia adelante
 anio = _dtDato[0:4]
 mes = _dtDato[5:7]
 dia = _dtDato[-2:]
 print("Year: " + str(anio))
 print("Month: " + str(mes))
 print("Day: " + str(dia))
# La variable (dtDato) almacena en int los caracteres extraidos de la variable (_dtDato)
 dtDato = datetime.datetime(int(anio), int(mes), int(dia))
# La función type() muestra el tipo de dato
 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))