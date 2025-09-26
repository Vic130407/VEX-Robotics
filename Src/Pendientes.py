pendientes = []
#Imprime todas las tareas registradas en el programa#
def mostrar_tareas():
    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(pendientes):
        estado = "Completada" if tarea[1] else "Pendiente"
        print(f"{i+1}. {tarea[0]} - {estado}")

#Cuenta las tareas y muestra un resumen indicando el total de tareas, las tareas completadas y las tareas pendientes#
def contar_tareas():
    total = len(pendientes)
    completadas = sum(1 for t in pendientes if t[1])
    print("\n--- Resumen ---")
    print("Total de tareas:", total)
    print("Tareas completadas:", completadas)
    print("Tareas pendientes:", total - completadas)

#Pregunta por una nueva tarea y la agrega al codigo#
def agregar_tarea():
    nueva = input("Escribe la nueva tarea: ")
    pendientes.append((nueva, False))
    print("Tarea agregada exitosamente")

#Pregunta al usuario por la tarea que desee marcar como completada y cambia su estado a True#
def completar_tarea():
    mostrar_tareas()
    try:
        num = int(input("Numero de la tarea que quieres marcar como completada: "))
    except ValueError:
        print("Por favor, ingresar un numero valido")
    else:
        if 1 <= num <= len(pendientes):
            tarea = pendientes[num-1][0]
            pendientes[num-1] = (tarea, True)
            print("Tarea marcada como completada")
        else:
            print("Numero invalido")

#Despliega un grafico de barra para mostrar las tareas completadas y pendientes#
def barra_progreso():
    total = len(pendientes)
    if total == 0:
        print("\n--- Barra de progreso ---")
        print("No hay tareas aún. Progreso: 0%")
        return
    
    completadas = sum(1 for t in pendientes if t[1])
    progreso = (completadas / total) * 100 
    barra_longitud = 20
    completados = int((progreso / 100) * barra_longitud)
    barra = "█" * completados + " " * (barra_longitud - completados)
    
    print("\n--- Barra de progreso ---")
    print(f"[{barra}] {progreso:.1f}% ({completadas}/{total} tareas)")


#Menu de tareas con el cual accedes a las demas funciones#
def menu_tareas():
    while True:
        print("\n--- Menu de pendientes ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Ver resumen")
        print("5. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            contar_tareas()
        elif opcion == "5":
            print("Saliendo del administrador de pendientes...")
            break
        else:
            print("Opcion invalida")