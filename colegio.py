# Un colegio tiene programado un pago de $5,500.00 para el dia 15 de febrero de 2020. 
# Si el pago es realizado despues de la fecha, se cobran $8 pesos por cada dia transcurrido.

# Módulo  para expresiones regulares
import re
# Módulo para datos datetime
import datetime

# Función que verifica si la fecha ingresada tiene formato (YYYY/MM/DD)
def fechavalida(fecha):
  # Uso de excepciones
  try:
     anio = int(fecha[0:4])
     mes = int(fecha[5:7])
     dia = int(fecha[-2:])
     datetime.date(anio,mes,dia)
  except ValueError:
    # Si ocurre el error "ValueError" se retorna False
     return False
  # Si no ocurre un error se retorna True 
  return True

# Función que convierte la cadena (YYYY/MM/DD) a datetime
def crearfecha(fecha):
     anio = int(fecha[0:4])
     mes = int(fecha[5:7])
     dia = int(fecha[-2:])
     return datetime.date(anio,mes,dia)

def main():
    # Valor del pago
    pago = 5500.00
    # Valor extra a pagar        
    extra = 8.00
    # Se declara variable de paso para capturar la fecha en que se realizó el pago
    _fechapago = ""
    # Variable que contiene la fecha programada para el pago
    fechaprogra = crearfecha("2020/02/15")
    # Bucle que pregunta la fecha hasta que sea correcta
    while True:
        _fechapago = input("Fecha en que realizo el pago (YYYY/MM/DD): ")
        # Se valida el formato de la fecha introducida
        if re.search("^[0-9]{4}/[0-9]{2}/[0-9]{2}$",_fechapago):
            # Se evaluan los digitos de la fecha
            if fechavalida(_fechapago):
                fechapago = crearfecha(_fechapago)
                break
                # Si las condiciones se cumplen el bucle finaliza con un "break"
            else:
                print ("Fecha invalida")
        else:
            print("El formato es incorrecto")
            
    # timedelta es un periodo de tiempo obtenido por una operacion entre fechas
    fechasresta = fechapago - fechaprogra
    pagofinal = 0.00
    
    # Si la diferencia de dias es mayor a "0" (15-15=0) el pago esta fuera de tiempo
    if fechasresta.days > 0:
        pagofinal = (pago + (fechasresta.days * extra))
    # Si se pagó en el dia programado el pago no cambia
    else:
        pagofinal = pago
    print("Pago ${:0,.2f}".format(pagofinal))