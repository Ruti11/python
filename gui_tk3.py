class Persona:

    def __init__(self, nombre): 
        self.nombre = nombre 


    def avanza(self): 
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre) 

    def avanza(self):
        print('Ando moviendome en mi bicicleta') 


if __name__ == '__main__':
    persona = Persona ('Rut') 
    persona.avanza()

    ciclista = Ciclista('Isaac') 
    ciclista.avanza()
    