class calculadora: 
    primer_numero = None
    segundo_numero = None
    resultado = None

    def __init__(self,p,s):
        self.primer_numero = p
        self.segundo_numero = s

    def sumar(self):
        self.resultado = self.primer_numero + self.segundo_numero 
    
    def restar(self):
        self.resultado = self.primer_numero - self.segundo_numero

    def multiplicar(self):
        self.resultado = self.primer_numero * self.segundo_numero 

    def dividir(self):
         if(self.segundo_numero != 0):
             self.resultado = self.primer_numero / self.segundo_numero 
         else:
             self.resultado = "No se puede dividir entre cero"

    def get_resultado(self):
        return self.resultado


n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese otro numero: "))

casio = calculadora(n1, n2)
casio.sumar()
print(casio.get_resultado())
casio.restar()
print(casio.get_resultado())
casio.multiplicar()
print(casio.get_resultado())
casio.dividir()
print(casio.get_resultado())

#comentario
print("Ahí tienes el resultado")



