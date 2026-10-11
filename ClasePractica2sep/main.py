from funcionmenu import mostrar_menu
from productos import (agregar_producto, buscar_por_precio, eliminar_producto, mostrar_producto, mostrar_por_precio, mostrar_estadisticas, buscar_producto)



def main():
    while True:
        mostrar_menu()

        op = input("Seleccionar: ").strip()#strip elimina espacios al principio y al final

        match op:
            case "1": 
                agregar_producto()
            case "2":
                mostrar_producto()
                




if __name__ =="__main__":#para que este archivo se comporte como un programa principal
        main()