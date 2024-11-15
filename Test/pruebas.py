import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from CRUD.CRUDutilities import CRUD
from CRUD.CRUDCliente import CRUDCLiente
from CRUD.CRUDFacturas import CRUDfacturas

Base_de_datos = CRUD()
facturas = CRUDfacturas()
clientes = CRUDCLiente()

lista_facturas_creadas = facturas.create()
lista_clientes_creados = clientes.create()

# Asociar clientes a la base de datos
for indice in lista_clientes_creados:
    Base_de_datos.agregar_cliente(lista_clientes_creados[indice])

# asociar facturas a clientes de la base de datos Factura[0] se asocia a Cliente[0] solo para la prueba
for indice in lista_facturas_creadas:
    Base_de_datos.asociar_factura(lista_clientes_creados[indice],lista_facturas_creadas[indice])



