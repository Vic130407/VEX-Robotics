#Este es el menú principal del programa
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
    try: #Usamos un try por si el usuario mete otro tipo de dato no valido 
        opcion = int(input("Selecciona una opción (1-5): ")) 
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    else: #Depende de la opción que elija el usuario en el menú es la sección a la que te llevará
        if opcion==1:
            from Menu_integrantes import menu_integrantes #Aquí importamos las funciones del menu de integrantes para poder trabajar con ellas
            menu_integrantes()
        elif opcion==2:
            from inventario import menu_inventario #Aquí importamos las funciones del menu de inventario, para poder trabajar con ellas
            menu_inventario()
        elif opcion==3:
            from Pendientes import menu_tareas #Aquí importamos las funciones del menu de tareas o lista de pendientes
            menu_tareas()
        elif opcion==4:
            from Pendientes import barra_progreso #Aquí importamos las funcion de la barra de progreso que trabaja en conjunto con las funciones de pendientes que importamos en la partr de arriba
            barra_progreso()
        elif opcion==5: 
            print("Saliendo del sistema de VEX ROBOTICS")
            break #Termina el programa y lo cierra
        else:
            print("Opcion no valida")
open("inventario.txt","w") #Este open tiene como proposito vaciar el archivo, y no dejar los datos registrados cada que se abra ek programa, ya que si se meten los mismos datos se sobreescribirian
