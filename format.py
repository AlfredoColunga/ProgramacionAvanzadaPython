# Notación húngara:
# i - int
# f - float

def main():
  print("==AREA TRIANGULO==")
  # Se solicita el ingreso de datos con una variable de paso (_variable)
  _iBase = input("Ingrese medida de base: ")
  # Los datos ingresados se convierten al tipo correcto de dato
  base = int(_iBase)
  _iAltura = input("Ingrese medida de altura: ")
  altura = int(_iAltura)
  area = (base*altura)/2
  resultado = ("Area: {2:0.4f} | Operacion: {0} por {1} entre dos")
  # El número dentro de las llaves corresponde al orden de las variables
  # {2:0.4f} indica la variable (2), el número de decimales a mostrar (0.4), dato float (f)
  print(resultado.format(base,altura,area))
  # Se indica la salida de datos con el orden correspondiente dentro de .format()