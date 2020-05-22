def main():
  # Programa para leer archivos csv

  # Libreria para acceder a archivos csv
  import csv

  with open("AnalisisCOVID19.csv") as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter="|")
    contador_lineas = 0
    for linea in lector_csv:
        if contador_lineas == 0:
            print(f'Column names are {", ".join(linea)}')
            contador_lineas += 1
        else:
            print(f'\t{linea[0]} works in the {row[1]} department, and was born in {linea[2]}.')
            contadoe_lineas += 1
    print(f'Processed {contador_lineas} lines.')