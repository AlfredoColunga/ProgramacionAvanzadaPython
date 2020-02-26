# Se importa el módulo requerido para usar usar datos tipo Date
import datetime
def main():
 # Los datos string se preguntan y procesan sin intermediación.
 strDato = input("Ingrese dato tipo string: ")
 # Los datos numéricos se preguntan por intermediación.
 intDato = input("Ingrese dato tipo entero: ")
 intDato = int(intDato)
 floatDato = input("Ingrese dato tipo float: ")
 floatDato = float(floatDato)
 # Los datos date se preguntan por intermediación.
 dateDato = input("Ingrese fecha (yyyy/mm/dd): ")
 # [n,m] Extrae de la posición n a la posición m,sin incluir m.
 # [-m:] Extrae desde la posición m, de atrás para adelante, hasta el final.
 anio = dateDato[0:4]
 mes = dateDato[5:7]
 dia = dateDato[-2:]
 print(anio)
 print(mes)
 print(dia)
 dateDato = datetime.datetime(int(anio), int(mes), int(dia))
 print(strDato)
 print(type(strDato))
 print(intDato)
 print(type(intDato))
 print(floatDato)
 print(type(floatDato))
 print(dateDato)
 print(type(dateDato))