# Escritura de archivo texto plano

# Modulo para trabajar con el sistema operativo
import os

# Modulo para trabajar con archivos csv
import csv

# Se declara clase Contacto
# <<clase Contacto>> sirve para poblar una lista que perimte manejar en memoria los datos.
# La lista se vaciía al archivo csv final del programa
class Contacto():
    def __init__(self, USUARIO, NOMBRE, CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO

# Lista en la cual vamos a trabajar con los Contactos
Contactos = []
# Se cargan dos elementos
Contactos.append(Contacto('master','José Ruiz','jose.ruiz@hotmail.com'))
Contactos.append(Contacto('student','Alma Pérez','almitarules@hotmail.com'))
# En el programa final, realmente la lista se carga a partir del CSV.

# Se guarda en la variable la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\contactos.csv"
archivo_respaldo=ruta+"\\contactos.bak"

# Se determina si el archivo de trabajo ya existe
if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifica si hay respaldo y lo borra
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

    # Establece el achivo de datos, como respaldo
    os.rename(archivo_trabajo,archivo_respaldo)

# Genera el archivo CSV
f = open(archivo_trabajo,"w+")
# Escribe los encabezados de mi csv
f.write("USUARIO|NOMBRE|CORREO\n")
# Se escribe en el csv, a partir de la lista de objetos
for elemento in Contactos:
    f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

# Se cierra el archivo
f.close()