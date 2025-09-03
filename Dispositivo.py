#Esta será la Superclase (o clase 'Padre'), es decir, de la cual heredearán los métodos y atributos las otras Subclases (o clases 'hijas')

class Dispositivo():
    def __init__(self, marca, modelo, precio): #método constructor para definirlo como un objeto con sus respectivos atributos (características) y métodos (acciones)
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio #encapsulamiento: atributo privado


    #crear método para obtener el precio (ya que no se puede acceder a él fuera de la clase por ser privado)
    def get_precio(self):
        return self.__precio
    
    
    #crear método (set) para modificar el precio (se agrega también un mensaje con la modificación)
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0: #condición para que se aplique el método solo si el nuevo precio es mayor que 0
            print("===============================================================")
            print(f"Se ha MODIFICADO el precio del dispositivo '{self.marca} {self.modelo}'")
            print(f"      Precio anterior: ${self.get_precio():,}".replace(",", ".")) #dar formato al precio para hacerlo más legible
            print(f"      Nuevo precio: ${nuevo_precio:,}".replace(",", "."))
            print("===============================================================")
            self.__precio = nuevo_precio #asignar el nuevo valor ('nuevo_precio') al atributo 'precio'


    #crear método que muestra la descripción del dispositivo, mostrando su marca y modelo
    def descripcion(self):
        return (f"Dispositivo\n"
                f"  Marca: {self.marca}\n"
                f"  Modelo: {self.modelo}")

'''
Todos los métodos y atributos (marca, modelo, precio) de esta superclase 'Dispositivo' serán HEREDADOS a las otras subclases (Telefono, Tablet, Computadora)
Los métodos también pueden ser reescritos por cada subclase (como se realizará con el método 'descripcion()') para que sea particular a cada una.

''' 