#importar todas las clases creadas (Clase: Tienda, Superclase: Dispositivo, Subclases: Computadora, Telefono, Tablet)

from Dispositivo import Dispositivo
from Computadora import Computadora
from Telefono import Telefono
from Tablet import Tablet
from Tienda import Tienda

#crear tienda y definirla como objeto tipo "Tienda" para poder acceder a sus métodos
tienda = Tienda()

#instanciar dispositivos
computadora = Computadora("Acer", "Nitro 5", 570000, 32)
telefono = Telefono("Xiaomi", "Redmi note 11 pro", 230990, 108)
tablet = Tablet("Samsung", "Galaxy S6", 214990, 10.4)


'''A continuación se cambiará el precio de una tablet utilizando método setter ('set_precio()')
Puede utilizarlo ya que 'tablet' es un objeto de tipo 'Tienda'
por lo que es subclase  de 'Dispositivo' y por tanto, hereda el método 'set_precio()' creado para esa Superclase 'Dispositivo'''

tablet.set_precio(199990)


#agregar vehiculos a la lista (método de la clase 'Tienda')
tienda.agregar_dispositivo(computadora)
tienda.agregar_dispositivo(telefono)
tienda.agregar_dispositivo(tablet)

#mostrar catálogo de dispositivos de la tienda (método de la clase 'Tienda')
tienda.mostrar_catalogo()
