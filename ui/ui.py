class UI:
    def mostrar_menu_principal(self):
        while True:
            try:
                print("="*80)
                print("\n\t\tBIENVENIDO AL SISTEMA GESTOR DE FACTURACION AGRICOLA\n")
                print("="*80 + "\n")
                print("1) Agregar cliente a la base de datos\n")
                print("2) Agregar producto a la base de datos\n")
                print("3) Buscar cliente y listar todas sus facturas\n")
                print("4) Eliminar cliente de la base de datos\n")
                print("5) Vender producto a un cliente\n\n")
    
                opcion_elegida_menu_principal = int(input("Digite la opción que desea realizar (1-5): "))
                if 1 <= opcion_elegida_menu_principal <= 5:
                    return opcion_elegida_menu_principal
                else:
                    print("Error: Opción fuera de rango. Debe ser un número entre 1 y 5.")
            except ValueError:
                print("Error: Entrada no válida. Debes ingresar un número entero.")

    def interfaz_agregar_cliente(self):
        print("\n" + "="*80)
        print("\t\tINFORMACIÓN DEL CLIENTE\n")
        print("\n" + "="*80)
        nombre_cliente = str(input("Digite el nombre completo del cliente: "))
        cedula_cliente = str(input("Digite la cedula del cliente: "))
        return nombre_cliente,cedula_cliente
        
    def menu_agregar_producto_control(self): 
        while True:
            try: 
                print("="*80)
                print("\n\t\tINFORMACIÓN DEL PRODUCTO\n")
                print("="*80 + "\n")
                print("1. Productos fertilizantes.\n")
                print("2. Productos plagas.\n\n")
                opcion_elegida_menu_producto = int(input("Digite la opción que desea realizar: "))
                if 1 <= opcion_elegida_menu_producto <= 2:
                    return opcion_elegida_menu_producto
                else:
                    print("Error: Opción fuera de rango. Debe ser un número entre 1 y .")
            except ValueError:
                print("Error: Entrada no válida. Debes ingresar un número entero.")
    
    def interfaz_agregar_producto_control(self, opcion_elegida_menu_producto):
        print("="*80)
        print("\n\t\tINGRESANDO DATOS DEL PRODUCTO\n")
        print("="*80 + "\n")
        nombre_producto = str(input("Nombre del producto: "))
        registro_ica = str(input("Registro ica: "))
        frecuencia_aplicacion = int(input("Frecuencia de aplicación del producto: "))
        precio_producto = float(input("Precio del producto: "))
        if opcion_elegida_menu_producto == 1:
            fecha_ultima_aplicacion = str(input("Fecha de la última publicación: "))
            return nombre_producto, registro_ica, frecuencia_aplicacion, precio_producto, fecha_ultima_aplicacion
        if opcion_elegida_menu_producto == 2:
            periodo_carencia = int(input("Periodo carencia: "))
            return nombre_producto, registro_ica, frecuencia_aplicacion, precio_producto,periodo_carencia

    def interfaz_buscar_cliente(self, crud):
        print("\n" + "="*80)
        print("\t\tBUSCAR CLIENTE Y LISTAR SUS FACTURAS\n")
        print("="*80)
        cedula_cliente = str(input("Digite la cédula del cliente: "))
        cliente = crud.buscar_por_cedula(cedula_cliente)
        
        if cliente:
            print(f"\nCliente encontrado: {cliente.nombre} (Cédula: {cliente.cedula})")
            print("\nFACTURAS DEL CLIENTE:")
            
            if not cliente.facturas:
                print("Este cliente no tiene facturas registradas.\n")
            else:
                for idx, factura in enumerate(cliente.facturas, start=1):
                    print(f"\nFactura #{idx}")
                    print(f"Fecha: {factura.fecha}")
                    print(f"Valor Total: ${factura.valor_total:.2f}")
                    print("Productos Comprados:")
                    
                    # Listar productos comprados en cada factura
                    for producto in factura.productos:
                        if hasattr(producto, 'registro_ica'):  # Producto de Control
                            print(f"  - {producto.nombre} (Registro ICA: {producto.registro_ica}) "
                                  f"Frecuencia: {producto.frecuencia_aplicacion} días, Precio: ${producto.valor:.2f}")
                        elif hasattr(producto, 'dosis'):  # Antibiótico
                            print(f"  - {producto.nombre} (Dosis: {producto.dosis}Kg) "
                                  f"Aplicable a: {producto.tipo_animal}, Precio: ${producto.precio:.2f}")
                    print("-" * 50)
        else:
            print("Cliente no encontrado.\n")


    def interfaz_eliminar_cliente(self):
        print("\n" + "="*80)
        print("\t\tELIMINAR CLIENTE\n")
        print("="*80)
        cedula_cliente = str(input("Digite la cédula del cliente a eliminar: "))
        return cedula_cliente
    
    def interfaz_vender_producto(self):
        print("\n" + "="*80)
        print("\t\tVENDER PRODUCTO A UN CLIENTE\n")
        print("="*80)
        cedula_cliente = str(input("Digite la cédula del cliente para la venta: "))
        return cedula_cliente


    
    


