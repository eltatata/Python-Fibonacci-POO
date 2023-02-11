class Fibonacci:
    def __init__(self):
        self.serie = [0, 1]
    
    def CreateSerie(self, terms):
            if terms <= 0:
                return "Numero de terminos invalido"
            elif terms == 1:
                return 0
            
            for num in range(terms - 2):
                self.serie.append(self.serie[num] + self.serie[num + 1])
            
            return self.serie