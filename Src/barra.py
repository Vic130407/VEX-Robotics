# MENÚ
print("="*45)
print("\t BINVENIDO A VEX: ROBOTICS")
print("\t\t-----MENÚ-----")
print("="*45)
print("1. Lista de integrantes por sector")
print("2. Inventario/Materiales")
print("3. Lista de pendientes")
print("4. Barra de progreso")
print("5. Salir")

#Tareas pendientes
pendientes = [
    ("Diseñar prototipo", False),
    ("Programar sensores", False),
    ("Revisar baterías", False)
]

# Estructura principal con while para el menú
opcion = ""
while opcion != "5":
    opcion = input("Seleccione una opción: ")

    if opcion == "3":
        # Lista de pendientes 
        print("Lista de pendientes:")
        for i, (tarea, completada) in enumerate(pendientes, 1):
            estado = "Completada" if completada else "Pendiente"
            print(f"{i}. {tarea} - {estado}")
        
        # Contar total de tareas
        total_tareas = len(pendientes)
        
        # Contar tareas completadas
        tareas_completadas = sum(1 for tarea in pendientes if tarea[1])
        
        print(f"\nTotal de tareas: {total_tareas}")
        print(f"Tareas completadas: {tareas_completadas}")

    elif opcion == "4":
        # Barra de progreso (usa la variable global pendientes)
        # Contar total de tareas
        total_tareas = len(pendientes)
        
        # Contar tareas completadas
        tareas_completadas = sum(1 for tarea in pendientes if tarea[1])
        
        # Calcular progreso como porcentaje
        if total_tareas > 0:
            progreso = (tareas_completadas / total_tareas) * 100
        else:
            progreso = 0
        
        print(f"\nProgreso general: {progreso:.1f}%")
        
        # Mostrar barra de progreso simple (texto-based, 20 caracteres de ancho)
        barra_longitud = 20
        completados = int((progreso / 100) * barra_longitud)
        barra = "█" * completados + " " * (barra_longitud - completados)
        print(f"[{barra}] {progreso:.1f}% ({tareas_completadas}/{total_tareas} tareas)")
        
        # Opcional: permitir actualizar estado de una tarea
        actualizar = input("¿Desea actualizar el estado de una tarea? (s/n): ")
        if actualizar.lower() == "s":
            print("Lista de tareas para actualizar:")
            for i, (tarea, completada) in enumerate(pendientes, 1):
                estado = "Completada" if completada else "Pendiente"
                print(f"{i}. {tarea} - {estado}")
            idx = int(input("Número de tarea a actualizar: ")) - 1
            if 0 <= idx < len(pendientes):
                nuevo_estado = input("¿Completada? (s/n): ")
                pendientes[idx] = (pendientes[idx][0], nuevo_estado.lower() == "s")
                print("Estado actualizado. (¡Ahora persiste en el programa!)")
            else:
                print("Índice inválido.")

    elif opcion == "5":
        print("¡Gracias por usar el gestor de proyectos VEX Robotics! Saliendo...")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione del 1 al 5.")
    
    # Reimprimir el menú solo si no se sale
    if opcion != "5":
        print("\n" + "="*45)
        print("\t\t-----MENÚ-----")
        print("="*45)
        print("1. Lista de integrantes por sector")
        print("2. Inventario/Materiales")
        print("3. Lista de pendientes")
        print("4. Barra de progreso")
        print("5. Salir")