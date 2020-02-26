def main():
  MedidaBase = 87
  MedidaAltura = 25
  AreaTriangulo = (MedidaBase*MedidaAltura)/2
  resultado = "Area de triangulo: {2:0.4f} ( {0} por {1} entre dos )"
  print(resultado.format(MedidaBase, MedidaAltura, AreaTriangulo))