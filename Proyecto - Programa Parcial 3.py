print(' ')
print('******************************************************************************')
print('*                                                                            *')
print('*                        BIENVENIDOS A TECNOMARKET                           *')
print('*                                                                            *')
print('******************************************************************************')

# Usuarios por defecto
usuarios = {'Alondra Lopez': {'nombre': 'Alondra Lopez', 'id': 1, 'edad': 30, 'nivel': 'Administrador', 'contraseña': 'admin'},
           'Oswaldo Monterroza': {'nombre': 'Oswaldo Monterroza', 'id': 2, 'edad': 30, 'nivel': 'Gerente', 'contraseña': '1234'},
           'Rene Lemus': {'nombre': 'Rene Lemus', 'id': 3, 'edad': 30, 'nivel': 'Gerente', 'contraseña': '4321'},
           'Norlin Calderon': {'nombre': 'Norlin', 'id': 4, 'edad': 30, 'nivel': 'Vendedor', 'contraseña': '4444'},
           'Erick Diaz': {'nombre': 'Erick Diaz', 'id': 5, 'edad': 30, 'nivel': 'Vendedor', 'contraseña': '1111'}}

# Niveles de usuario
niveles = ['Administrador', 'Gerente', 'Vendedor']

# Areas 
areas = ['PCs', 'Moviles']

# Categorias
categorias = {'Laptops': {'area':'PCs'}, 'Desktops': {'area':'PCs'}, 
              'Celulares':{'area':'Moviles'}, 'Tablets':{'area':'Moviles'}}

# Productos
productos = {'Laptop ASUS': {'nombre': 'Laptop ASUS', 'proveedor': 'ASUS', 'fecha_entrada': '12/05/2023', 'garantia': '1 año', 'detalles': 'Color negro, Disco SSD 500 GB, 12GB RAM', 'precio': 1200, 'unidades': 8, 'categoria': 'Laptops'}, 
             'Lenovo ThinkPad': {'nombre': 'Lenovo ThinkPad', 'proveedor': 'Lenovo', 'fecha_entrada': '19/05/2023', 'garantia': '3 años', 'detalles': 'Color gris, SSD 1 TB, 16GB RAM', 'precio': 1500, 'unidades': 5, 'categoria': 'Laptops'},
             'Dell Inspiron Desktop': {'nombre': 'Dell Inspiron Desktop', 'proveedor': 'Dell', 'fecha_entrada': '13/05/2023', 'garantia': '2 años', 'detalles': 'Color negro, HDD 1 TB, 8GB RAM', 'precio': 800, 'unidades': 12, 'categoria': 'Desktops'},
             'Computadora HP': {'nombre': 'Computadora HP', 'proveedor': 'HP', 'fecha_entrada': '15/05/2023', 'garantia': '2 años', 'detalles': 'Color rojo, SSD 250 GB, 8GB RAM', 'precio': 1000, 'unidades': 10, 'categoria': 'Desktops'},
             'Samsung Galaxy S21': {'nombre': 'Samsung Galaxy S21', 'proveedor': 'Samsung', 'fecha_entrada': '14/05/2023', 'garantia': '1 año', 'detalles': 'Color blanco, 128 GB de almacenamiento, 8GB RAM', 'precio': 900, 'unidades': 20, 'categoria': 'Celulares'},
             'iPhone 13 Pro': {'nombre': 'iPhone 13 Pro', 'proveedor': 'Apple', 'fecha_entrada': '14/05/2023', 'garantia': '2 años', 'detalles': 'Color dorado, 256 GB de almacenamiento interno, 6GB RAM', 'precio': 1200, 'unidades': 10, 'categoria': 'Celulares'},
             'Samsung Galaxy Tab S7': {'nombre': 'Samsung Galaxy Tab S7', 'proveedor': 'Samsung', 'fecha_entrada': '10/05/2023', 'garantia': '1 año', 'detalles': 'Pantalla de 11 pulgadas, 128 GB de almacenamiento', 'precio': 800, 'unidades': 8, 'categoria': 'Tablets'},
             'Tablet iPad Pro': {'nombre': 'Tablet iPad Pro', 'proveedor': 'Apple', 'fecha_entrada': '10/05/2023', 'garantia': '1 año', 'detalles': 'Color gris, Pantalla de 12.9 pulgadas, 256 GB de almacenamiento', 'precio': 1300, 'unidades': 15, 'categoria': 'Tablets'}}

# Funcion para registrar usuarios
def registrar_usuario():
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Registrar usuario ***')
    # Solicitar los datos del usuario
    id = int(input('\nIngrese el ID: '))
    nombre = str(input('Ingrese el nombre de usuario: ')).strip() 
    edad = int(input('Ingrese su edad: '))
    contraseña = str(input('Ingrese la contraseña: ')).strip()
    # Listar niveles
    print('\nNiveles de acceso disponibles: \n')
    for nivel in niveles:
        print('-', nivel)
    # Solicitar el ingreso del nivel que tendra el usuario
    nivel = str(input('\nIngrese el nivel de acceso del usuario: ')).strip()
    while nivel not in niveles:
        print('| Opción incorrecta. Inténtelo de nuevo |')
        nivel = str(input('\nIngrese el nivel de acceso del usuario: ')).strip()
    # Agregar usuario al diccionario de usuarios
    usuarios[nombre] = {'nombre': nombre, 'id': id, 'edad': edad, 'contraseña': contraseña, 'nivel': nivel}
    print('\n\t\t\t*** Usuario guardado ***')
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para mostrar los usuarios registrados
def mostrar_usuarios():
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t*** Lista de usuarios registrados ***')
    for usuario in usuarios.values():
        print('\n- Nombre: ', usuario['nombre'])
        print('ID: ', usuario['id'])
        print('Edad: ', usuario['edad'])
        print('Nivel: ', usuario['nivel'])
        print('Contraseña: ', usuario['contraseña'])
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para mostrar las areas almacenadas
def mostrar_areas():
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Áreas registradas ***')
    for area in areas:
        print(f'\nNombre: {area}')
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para mostrar las categorias almacenadas
def mostrar_categorias():
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Categorias registradas ***')
    for categoria, datos in categorias.items():
        print(f'\nNombre: {categoria} | Área: {datos["area"]}')
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para mostrar los productos almacenados
def mostrar_productos():
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Lista de productos ***')
    for producto in productos.values():
        print('\nNombre del producto: ', producto['nombre'])
        print('Proveedor: ', producto['proveedor'])
        print('Fecha de entrada: ', producto['fecha_entrada'])
        print('Garantia: ', producto['garantia'])
        print('Detalles: ', producto['detalles'])
        print('Precio: $', producto['precio'])
        print('Unidades: ', producto['unidades'])
        print('Categoría: ', producto['categoria'])
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para crear area
def crear_area():
        print(' ')
        print('-----------------------------------------------------------------------------------')
        print('\n\t\t\t*** Registrar área ***')
        while True:
            nombre_area = str(input('\nIngrese el nombre del área: ')).strip()
            if nombre_area in areas:
                print('| El área ya existe. Ingrese otro nombre para el área |')
            else:
                # Se guarda el area
                areas.append(nombre_area)
                print('\n\t\t*** El área ha sido creada ***')
                break
        print(' ')
        print('-----------------------------------------------------------------------------------')

# Función para crear una categoria y agregarla a una área existente
def crear_categoria():
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Registrar categoria ***')
    while True:
        # Muestra el listado de las áreas disponibles
        print('\nÁreas disponibles: \n')
        for area in areas:
            print('-', area)
        area = str(input('\nIngrese el área a la que desea agregar la categoría: ')).strip() 
        if area not in areas:
            print('| El área no existe. Ingrese otro nombre |')
        else:
            while True:
                nombre_categoria = str(input('\nIngrese el nombre de la categoría: ')).strip()
                if nombre_categoria in categorias:
                    print('| La categoría ya existe. Ingrese otro nombre |')
                else:
                    # Se guarda la categoria
                    categorias[nombre_categoria] = {'area': area}
                    print(f'\n\t*** La categoría "{nombre_categoria}" ha sido creada en el área "{area}" ***')
                    break
            break
    print(' ')
    print('-----------------------------------------------------------------------------------')

# Función para crear un producto           
def crear_producto():
        print(' ')
        print('-----------------------------------------------------------------------------------')
        print('\n\t\t\t*** Registrar producto ***')
        nombre_producto = str(input('\nIngrese el nombre del producto: '))
        proveedor = str(input('Ingrese el proveedor del producto: '))
        fecha_entrada = str(input('Ingrese la fecha de entrada del producto (en formato dd/mm/aaaa): '))
        garantia = str(input('Ingrese el periodo de garantia del producto: '))
        detalles = str(input('Ingrese los detalles del producto: '))
        precio = f"{float(input('Ingrese el precio del producto: $')):,.2f}"
        unidades = int(input('Ingrese las unidades disponibles del producto (ingrese un número entero): '))
        # Muestra el listado de las categorias disponibles
        while True:
            print('\nCategorias disponibles: \n')
            for categoria in categorias:
                print('-', categoria)
            categoria = str(input('\nIngrese la categoria a la que desea agregar el producto: ')).strip()
            if categoria in categorias:
            # Se guarda el producto
                productos[nombre_producto] = {'nombre': nombre_producto, 'proveedor': proveedor, 'fecha_entrada': fecha_entrada, 'garantia': garantia, 'detalles': detalles, 'precio': precio, 'unidades': unidades, 'categoria': categoria}
                print('\n\t\t*** El producto ha sido creado ***')
                break
            else:
                print('| La categoria no existe. Ingrese un nombre válido |')
        print(' ')
        print('-----------------------------------------------------------------------------------')
    
# Función para realizar una venta
def venta(areas, categorias):
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('\n\t\t\t*** Registrar venta ***')
    # Seleccionar área
    while True:
        print('\nÁreas disponibles: \n')
        for area in areas:
            print('-', area)
        area = str(input('\nSeleccione un área: '))
        if area not in areas:
            print('| El área seleccionada no es válida. Intente de nuevo |')
        else:
            break
                    
    # Seleccionar categoría dentro del área seleccionada
    categorias_area = [nombre for nombre, datos in categorias.items() if datos['area'] == area]
    while True:
        print(f'\nCategorías disponibles en el área "{area}": \n')
        for categoria in categorias_area:
            print('-', categoria)
        nombre_cat = str(input('\nIngrese una categoría: ')).strip()
        if nombre_cat not in categorias_area:
            print('| La categoría ingresada no es válida. Intente de nuevo |')
        else:
            break
    
    # Mostrar los productos relacionados a esa categoria
    while True:
        productos_categoria = [nombre for nombre, datos in productos.items() if datos['categoria'] == nombre_cat]
        print(f'\nProductos disponibles en la categoría "{nombre_cat}": ')
        print(' ')
        print('-----------------------------------------------------------------------------------')
        print('\n\t\t\t*** Lista de productos ***')
        for producto in productos_categoria:
            print('\n-', producto)
            print('Proveedor: ', productos[producto]['proveedor'])
            print('Fecha de entrada: ', productos[producto]['fecha_entrada'])
            print('Garantia: ', productos[producto]['garantia'])
            print('Detalles: ', productos[producto]['detalles'])
            print('Precio: $', productos[producto]['precio'])
            print('Unidades: ', productos[producto]['unidades'])
            print('Categoría: ', productos[producto]['categoria']) 
        
        # Hacer la seleccion para la venta    
        productos_vendidos = {}
        while True:
            while True:
                print(' ')
                print('-----------------------------------------------------------------------------------')
                producto_seleccionado = str(input('\nSeleccione un producto para agregar a la venta (o ingrese "o" para terminar): ')).strip()
                if producto_seleccionado == 'o':
                    if len(productos_vendidos) == 0:
                        print('| Debe agregar al menos un producto a la venta |')
                        continue
                    else:
                        break
                elif producto_seleccionado not in productos_categoria:
                    print('| El producto seleccionado no es válido. Intente de nuevo |')
                else:
                    cantidad = int(input(f'\nIngrese la cantidad de "{producto_seleccionado}" que desea agregar a la venta: '))
                    if cantidad > [producto_seleccionado]['unidades']:
                        print(f"| No hay suficientes unidades disponibles de {producto_seleccionado} |")
                    else:
                        if producto_seleccionado in productos_vendidos:
                            productos_vendidos[producto_seleccionado] += cantidad
                        else:
                            productos_vendidos[producto_selecci"onado] = cantidad
                            productos[producto_seleccionado]["unidades] -= cantidad
                        print(f'\n| Se han agregado {cantidad} "{producto_seleccionado}" a la venta |')
        
            print('\nLista de compras: ')
            print("------------------------------------")
            print("|Producto       |Cantidad |Precio  |")
            print("|---------------|---------|--------|")
            for producto, cantidad in productos_vendidos.items():
                precio = productos[producto]["precio"] 
                print(f"|{producto:<15}|{cantidad:^9}|{precio:>8.2f}|")
            print("|---------------|---------|--------|")
            
            respuesta = str(input('\n¿Desea agregar más productos a la venta? (s/n): ')).strip()
            if respuesta.lower() == 's':
                print(f'\nProductos disponibles en la categoría "{nombre_cat}": ')
                print(' ')
                print('-----------------------------------------------------------------------------------')
                print('\n\t\t\t*** Lista de productos ***')
                for producto in productos_categoria:
                    print('\n-', producto)
                    print('Proveedor: ', productos[producto]['proveedor'])
                    print('Fecha de entrada: ', productos[producto]['fecha_entrada'])
                    print('Garantia: ', productos[producto]['garantia'])
                    print('Detalles: ', productos[producto]['detalles'])
                    print('Precio: $', productos[producto]['precio'])
                    print('Unidades: ', productos[producto]['unidades'])
                    print('Categoría: ', productos[producto]['categoria'])
                    continue
            else:
                break
                
        # Calcular el precio total de la venta
        precio_total = 0
        for producto, cantidad in productos_vendidos.items():
            precio_total += productos[producto]['precio'] * cantidad
        break
            
    # Mostrar el resumen de la venta
    print("\nResumen de la venta:")
    print("------------------------------------")
    print("|Producto       |Cantidad |Precio  |")
    print("|---------------|---------|--------|")
    for producto, cantidad in productos_vendidos.items():
        precio = productos[producto]["precio"] 
        print(f"|{producto:<15}|{cantidad:^9}|{precio:>8.2f}|")
    print("|---------------|---------|--------|")
    print(f"|Total          |         |{precio_total:>8.2f}|")
    print("------------------------------------")
    print('\n\t\t\t*** Venta realizada con exito ***')
    print(' ')
    print('-----------------------------------------------------------------------------------')
    return

def programa_principal():
    # Menu de inicio
    while True:
        print('''\n¿Que desea hacer?: \n 
        1. Iniciar sesión
        2. Salir''')

        opcion1 = int(input('\nSeleccione una opción: '))

        if opcion1 == 1:
            print('-----------------------------------------------------------------------------------')
            print('\n\t\t\t*** Iniciar sesión ***')
            # Solicitar los datos del usuario
            nombre_usuario = str(input('\nIngrese su nombre de usuario: ')).strip()
            contraseña = str(input('Ingrese su contraseña: ')).strip()
            # Verificar si el nombre de usuario y la contraseña coinciden con los datos almacenados en el diccionario de usuarios
            if nombre_usuario in usuarios and usuarios[nombre_usuario]['contraseña'] == contraseña:
                # Si los datos coinciden, se inicia la sesión
                print('\n\t\t*** Ha iniciado sesión correctamente ***')
                print(' ')
                print('-----------------------------------------------------------------------------------')

                # Menu de opciones dependiendo del nivel del usuario que ha iniciado sesión
                if usuarios[nombre_usuario]['nivel'] == 'Administrador':
                    print('\nSu nivel de acceso es:', usuarios[nombre_usuario]['nivel'])
                    while True:
                        print('\n\t\t*** ACTUALMENTE SE ENCUENTRA TRABAJANDO ***')
                        print('\nMenu de opciones: ')
                        print('\n        1. Crear área')
                        print('        2. Crear categoría')
                        print('        3. Crear producto')
                        print('        4. Registrar usuario')
                        print('        5. Salir')

                        opcion2 = int(input('\nSeleccione una opción: '))
                        
                        if opcion2 == 1:
                            crear_area()
                        elif opcion2 == 2:
                            crear_categoria()
                        elif opcion2 == 3:
                            crear_producto()
                        elif opcion2 == 4:
                            registrar_usuario()
                        elif opcion2 == 5:
                            print('\n\t\t\t*** Sesión cerrada ***')
                            print(' ')
                            print('-----------------------------------------------------------------------------------')
                            break
                        
                elif usuarios[nombre_usuario]['nivel'] == 'Gerente':
                    print('\nSu nivel de acceso es:', usuarios[nombre_usuario]['nivel'])
                    while True:
                        print('\n\t\t*** ACTUALMENTE SE ENCUENTRA TRABAJANDO ***')
                        print('\nMenu de opciones: ')
                        print('\n        1. Ver áreas')
                        print('        2. Ver categorías')
                        print('        3. Ver productos')
                        print('        4. Ver usuarios')
                        print('        5. Salir')

                        opcion2 = int(input('\nSeleccione una opción: '))

                        if opcion2 == 1:
                            mostrar_areas()
                        elif opcion2 == 2:
                            mostrar_categorias()
                        elif opcion2 == 3:
                            mostrar_productos()
                        elif opcion2 == 4:
                            mostrar_usuarios()
                        elif opcion2 == 5:
                            print('\n\t\t\t*** Sesión cerrada ***')
                            print(' ')
                            print('-----------------------------------------------------------------------------------')
                            break

                elif usuarios[nombre_usuario]['nivel'] == 'Vendedor':
                    print('\nSu nivel de acceso es:', usuarios[nombre_usuario]['nivel'])
                    while True:
                        print('\n\t\t*** ACTUALMENTE SE ENCUENTRA TRABAJANDO ***')
                        print('\nMenu de opciones: ')
                        print('\n        1. Realizar venta')
                        print('        2. Salir')

                        opcion2 = int(input('\nSeleccione una opción: '))

                        if opcion2 == 1:
                            venta(areas, categorias)
                        elif opcion2 == 2:
                            print('\n\t\t\t*** Sesión cerrada ***')
                            print(' ')
                            print('-----------------------------------------------------------------------------------')
                            break

                else:
                    print('\n| No tiene permisos suficientes para acceder a las opciones del menú |')
                    print('\n\t\t\t*** Sesión cerrada ***')
                    print(' ')
                    print('-----------------------------------------------------------------------------------')
            
            # Si el usuario ingresa mal sus credenciales lo regresa al primer menu
            else:
                print('\n| Nombre de usuario o contraseña incorrecta |')

        elif opcion1 == 2:
            print('\n*** CERRANDO EL SISTEMA. VUELVA PRONTO ***')
            print(' ')
            break
        else:
            print('\nOpción no válida')

# Se llama a la función principal para iniciar la ejecución del programa       
programa_principal()