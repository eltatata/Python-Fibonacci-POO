from module_fibonacci import fibonacci
from POO_fibonacci import Fibonacci

while True:
    try:
        numRange = int(input("Cantidad de numero en la serie: "))
        serie = fibonacci(numRange)
        print(serie)

        serie = Fibonacci().CreateSerie(numRange)
        print(serie)
        
        break
    except ValueError:
        print("Debe ingresar valores numericos enteros\n")