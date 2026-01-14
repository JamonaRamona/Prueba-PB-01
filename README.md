# Sistema de Gestión de Tienda de Dispositivos

Sistema de gestión de inventario para una tienda de dispositivos electrónicos desarrollado en Python utilizando Programación Orientada a Objetos (POO).

## Descripción

Este proyecto implementa un sistema de catálogo para gestionar dispositivos electrónicos (computadoras, teléfonos y tablets) aplicando los principales conceptos de POO: **Herencia**, **Polimorfismo** y **Encapsulamiento**.

## Características

- **Gestión de dispositivos**: Agregar y listar dispositivos electrónicos
- **Cálculo automático**: Calcula el valor total del inventario
- **Modificación de precios**: Sistema seguro para actualizar precios con validaciones
- **Formato de moneda**: Presentación clara de precios con separadores de miles

## Tecnologías Utilizadas

- Python 3.12.7
- Programación Orientada a Objetos (POO)

## Estructura del Proyecto

```
├── Dispositivo.py    # Clase padre con atributos y métodos base
├── Computadora.py    # Subclase para computadoras
├── Telefono.py       # Subclase para teléfonos
├── Tablet.py         # Subclase para tablets
├── Tienda.py         # Clase para gestión del catálogo
└── main.py           # Archivo principal de ejecución
```

## Cómo Ejecutar

```bash
python main.py
```

## Conceptos de POO Aplicados

### Herencia
Las clases `Computadora`, `Telefono` y `Tablet` heredan de la clase padre `Dispositivo`, compartiendo atributos y métodos comunes.

### Polimorfismo
Cada subclase redefine el método `descripcion()` para mostrar información específica de cada tipo de dispositivo.

### Encapsulamiento
El atributo `precio` es privado (`__precio`) y solo es accesible mediante métodos getter y setter, garantizando la integridad de los datos.

## Ejemplo de Salida

```
======== DISPOSITIVO AGREGADO ========

Computadora
      Marca: Acer
      Modelo: Nitro 5
      RAM: 32 GB
      Precio: $570.000

====== CATÁLOGO DE DISPOSITIVOS ======

Computadora
      Marca: Acer
      Modelo: Nitro 5
      RAM: 32 GB
      Precio: $570.000

Tablet
      Marca: Xiaomi
      Modelo: Redmi note 11 pro
      Resolución cámara: 108 mp
      Precio: $230.990

Tablet
      Marca: Samsung
      Modelo: Galaxy S6
      Tamaño pantalla: 10.4 pulgadas
      Precio: $199.990

===== VALOR TOTAL DEL INVENTARIO: $1.000.980 =====
```

## Autor

**Araceli Alvarado**
- Estudiante de Analista Programador

*Este es un proyecto de aprendizaje y representa mi trabajo durante la etapa inicial de mi formación profesional.*

