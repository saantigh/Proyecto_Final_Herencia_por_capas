from Modelo.cliente import Cliente
from Modelo.factura import Factura
from CRUD.CRUD import CRUD
from ui.ui import UI

def main():
    # Se instancian las clases
    crud = CRUD()
    ui = UI()
    opcion = 0
    if True:
        while opcion>4 or opcion<1:
            opcion = ui.menu_agregar_producto_control()
    #         opcion = ui.mostrar_menu_principal()
        


    

    # Hacer debug para inspeccionar las composiciones
   # import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()