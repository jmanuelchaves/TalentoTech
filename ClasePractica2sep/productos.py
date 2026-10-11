
productos = []

def agregar_producto():

    try:#con el try/except el programa continua... si no estuviera, con cada error, tendría un cierre abrupto
        nombre = input("Nombre de producto : \n").strip()
        if not nombre:
            print("Error: el nombre no debe estar vacío")
            return
        precio = float(input("Precio \n"))
        cantidad = int(input("Cantidad \n"))

        if precio < 0:
            print("El precio no puede ser menor a 0")
            return
        if cantidad < 0:
            print("La cantidad no puede ser menor a 0")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(producto)

        print(f"Producto: '{producto}' se agregó correctamente ")

    except ValueError:
        print("Error, debes ingresar valores numéricos")
    finally:
        print("Operación terminada")


def mostrar_producto():
    print()

def buscar_producto():
    print()

def eliminar_producto():
    print()




def buscar_por_precio():
    print()


def mostrar_por_precio():
    print()


def mostrar_estadisticas():
    print()