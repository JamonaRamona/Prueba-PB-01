#Importar la clase 'Dispositivo' ya que en la clase 'Tienda' se utilizará el método 'descripcion()' de la clase 'Dispositivo'
#En este caso no se utiliza el principio de HERENCIA como en las clases anteriores, solo se hace referencia a ese método

from Dispositivo import Dispositivo

#crear clase Tienda
class Tienda:
    def __init__(self): #método constructor para crear la clase Tienda
        self.dispositivos = [] #inicializa con una lista vacía que almacenará los dispositivos
    
    #metodo que agrega dispositivos a la lista
    def agregar_dispositivo(self, dispositivo):
        
        print("\n======== DISPOSITIVO AGREGADO ========\n")
        print(f"{dispositivo.descripcion()}\n" #cada subclase (cada dispositivo) imprime su propio método de 'descripción' (polimorfismo)
              f"      Precio: ${dispositivo.get_precio():,}".replace(",", ".")) #dar formato al precio para hacerlo legible
        self.dispositivos.append(dispositivo) #agregar el dispositivo a la lista 'dispositivos'
    
    #método que recorre la lista 'dispositivos' y muestra la respectiva descripción y precio del dispositivo
    def mostrar_catalogo(self):
        print("\n====== CATÁLOGO DE DISPOSITIVOS ======\n")
        
        total = 0 #inicializar en cero el valor del inventario para que se adquiera luego el valor de la suma en cada iteración
        
        for d in self.dispositivos: #recorrer la lista 'dispositivos'
            print(f"{d.descripcion()}\n" #para cada elemento de la lista, llamar al método 'descripcion()' para que cada elemento utilice su propio método
                  f"      Precio: ${d.get_precio():,}".replace(",", ".")+ "\n") #dar formato al precio para hacerlo legible
            total = total + d.get_precio() #asignar nuevo valor al total del valor del inventario, siendo ahora la suma de todos los precios de los elementos de la lista
            
        print(f"===== VALOR TOTAL DEL INVENTARIO: ${total:,}".replace(",", ".") + " =====") #mostrar valor del inventario