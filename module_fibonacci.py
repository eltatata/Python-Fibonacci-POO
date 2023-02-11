def fibonacci(n):
    if n <= 0:
        return "Numero de terminos invalido"
    elif n == 1:
        return 0
    
    listSerie = [0, 1]
    
    for num in range(n - 2):
        listSerie.append(listSerie[num] + listSerie[num + 1])
    
    return listSerie