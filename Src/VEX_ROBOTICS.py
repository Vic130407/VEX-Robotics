while True:
    print()
    print("="*50)
    print("\tGESTOR DE PROYECTOS VEX ROBOTICS")
    print("="*50)
    print("1. Lista de integrantes")
    print("2. Inventario")
    print("3. Lista de pendientes")
    print("4. Barra de progreso")
    print("5. Salir")
    print("="*50)
    try:
        opcion = int(input("Selecciona una opción (1-5): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    else:
        if opcion==1:
            from Menu_integrantes import menu_integrantes
            menu_integrantes()
        elif opcion==2:
            from inventario import menu_inventario
            menu_inventario()
        elif opcion==3:
            from Pendientes import menu_tareas
            menu_tareas()
        elif opcion==4:
            from Pendientes import barra_progreso
            barra_progreso()
        elif opcion==5:
            print("Saliendo del sistema de VEX ROBOTICS")
            break
        else:
            print("Opcion no valida")