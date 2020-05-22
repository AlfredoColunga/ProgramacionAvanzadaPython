# Una variable global es una variable declarada fuera del procedimiento
variableglobal = "Variable global"
# Si se quiere usar esta variable dentro de las funciones se debe anteponer la palabra
# reservada "global"

def pendiente():
  pass
  # Una función debe llevar codigo. Si por el momento no existe codigo se usa "pass"
 
def sinargumentos():
  # Version local de "variableglobal"
  variableglobal = 101
  print("No recibe argumentos")
  print(variableglobal)
# sinargumentos() <-- Se llama a la función

# Los argumentos se muestran dentro de parentesis y van separados por ","
def recibeargumentos(fname,lname):
  print("Nombre: " + str(fname) + " " + str(lname))
  print(variableglobal)
# recibeargumentos("Alfredo","Colunga") <-- Se llama a la función

# Un argumento opcional es al que se le agrega un valor 
# El argumento opcional siempre van al final de la lista de argumentos
def argumentoopcional(ciudad,pais = "Mexico"):
  print("Soy de: " + str(ciudad) + ", " + str(pais))
# argumentoopcional("Nuevo Leon") <-- Se llama a la función

# "return" retorna valores
def usoreturn(x):
  return x * 2
# print(usoreturn(2)) <-- Se llama a la función
# print(usoreturn(3)) <-- Se llama a la función
# print(usoreturn(4)) <-- Se llama a la función

def main():
  # sinargumentos()
  # recibeargumentos("Alfredo","Colunga")
  # argumentoopcional("Nuevo Leon")
  print(usoreturn(2))
  print(usoreturn(3))
  print(usoreturn(4))
