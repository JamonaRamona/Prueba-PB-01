#importar Superclase (o clase 'Padre') de la cual la nueva clase 'Computadora' heredará sus atributos y métodos
from Dispositivo import Dispositivo

class Computadora(Dispositivo): 
    def __init__(self, marca, modelo, precio, ram):
        super().__init__(marca, modelo, precio) #hereda los atributos de la superclase 'Dispositivo'
        self.ram = ram #se añade un nuevo atributo particular para esta subclase
    
    #se modificará el método 'descripción()' de la superclase para que al llamarlo, imprima los atributos de esta clase (es decir, ahora muestre la RAM)
    #esto es por el principio de POLIMORFISMO
    def descripcion(self):
        return (f"Computadora\n"
                f"      Marca: {self.marca}\n"
                f"      Modelo: {self.modelo}\n"
                f"      RAM: {self.ram} GB")