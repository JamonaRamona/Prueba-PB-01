#importar Superclase (o clase 'Padre') de la cual la nueva clase 'Tablet' heredará sus atributos y métodos
from Dispositivo import Dispositivo

class Tablet(Dispositivo):
    def __init__(self, marca, modelo, precio, pulgadas):
        super().__init__(marca, modelo, precio) #hereda los atributos de la superclase 'Dispositivo'
        self.pulgadas = pulgadas #se añade un nuevo atributo ''pulgadas') para esta subclase
    
    #se modificará el método 'descripción()' de la superclase para que al llamarlo, imprima los atributos de esta clase (es decir, ahora muestre la RAM)
    #esto es por el principio de POLIMORFISMO
    def descripcion(self):
        return (f"Tablet\n"
                f"      Marca: {self.marca}\n"
                f"      Modelo: {self.modelo}\n"
                f"      Tamaño pantalla: {self.pulgadas} pulgadas")