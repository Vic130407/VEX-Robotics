integrantes = [
        {"MATRICULA": "AL07165261", "NOMBRE": "David Duran Rubio", "ROL": "Mecánica", "SEMESTRE": "Primer semestre"},
        {"MATRICULA": "AL07165262", "NOMBRE": "Victor Hernandez", "ROL": "Programación", "SEMESTRE": "Primer semestre"},
        {"MATRICULA": "AL07165263", "NOMBRE": "Blanca Dennis", "ROL": "Administración", "SEMESTRE": "Primer semestre"}
] #En esta lista estamos guardando diccionarios con los datos de los integrantes. (Los datos que esta aquí ahorita no son relevantes solo era para hacer pruebas)
def menu_integrantes():
    while True: #Aquí inicia el menú de la sección de integrantes 
        print()
        print("\t--- MENU: LISTA DE INTEGRANTES ---")
        print("1. Mostrar lista")
        print("2. Agregar integrante")
        print("3. Volver al menú principal")
        
        try:
            opcion = int(input("Selecciona una opción (1-3): ")) #El try que tenemos aquí cumple como proposito cuidar que el usuario ingrese un dato erroneo o no esperado
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        #Depende de la opción que decida será la función que mandaremos a llamar 
        if opcion == 1:
            mostrar_lista_integrantes()
        elif opcion == 2:
            agregar_integrante()
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_lista_integrantes(): #Esta función muestra la lista de integrantes, pero aplica un filtro por si es que quieres buscar en una sección en especifico.
    print("\n\t---  LISTA DE INTEGRANTES ---")
    print("1. General")
    print("2. Administración")
    print("3. Mecánica")
    print("4. Programación")
    
    try:
        opcion = int(input("Selecciona una opción (1-4): ")) #El try que tenemos aquí cumple como proposito cuidar que el usuario ingrese un dato erroneo o no esperado
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    
    if opcion == 1:
        filtro = "General" #En general muestra a todos los integrantes 
    elif opcion == 2:
        filtro = "Administración" #Aquí solo mostrara la sección de Administración 
    elif opcion == 3:
        filtro = "Mecánica" #Aquí solo mostrara la sección de Mecánica 
    elif opcion == 4:
        filtro = "Programación" #Aquí solo mostrara la sección de Programación 
    else:
        print("Opción no válida.")
        return
    
    print(f"{"MATRÍCULA":<12}{"NOMBRE":<25}{"ROL":<15}{"SEMESTRE":<15}") #Aqui muestra la lista pero deja los espacios necesarios paa que se vea ordenado
    print("-" * 65)
    for integrante in integrantes:
        if filtro == "General" or integrante["ROL"] == filtro: #En esta parte del codigo es donde se hace el filtro como tal, ya que en la sección de arriba se de arriba se decide la vista →
            print(f"{integrante["MATRICULA"]:<12} {integrante["NOMBRE"]:<25} {integrante["ROL"]:<15} {integrante["SEMESTRE"]:<15}") #→ Y en esta parte del codigo se imprimen los datos con la vista o filtro deseados

def agregar_integrante(): #Aqui agregas un nuevo integrante 
    print("\n\t--- AGREGAR NUEVO INTEGRANTE ---")
    matricula = input("Matrícula: ") #Te pide los datos necesarios
    nombre = input("Nombre: ")
    print("Roles disponibles:") #Aquie en los roles para que no hubiese errores o confusión a la hora de escribir los roles, decidimos mejor que el usuario los escoja al seleccionar un numero
    print("1. Administración")
    print("2. Mecánica")
    print("3. Programación")
    
    try:
        rol_opcion = int(input("Selecciona el rol (1-3): ")) #Aqui cuidamos que el usuario no ingrese algun rol de manera erronea
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    
    if rol_opcion == 1:
        rol = "Administración"
    elif rol_opcion == 2:
        rol = "Mecánica"
    elif rol_opcion == 3:
        rol = "Programación"
    else:
        print("Opción no válida.")
        return
    semestre = input("Semestre: ")
    
    confirmacion = input("¿Deseas guardar este registro? (s/n): ").lower() #En esta parte confirmamos el registro para guardarlos.
    if confirmacion == 's' or confirmacion=="S":
        integrantes.append({
            "MATRICULA": matricula,
            "NOMBRE": nombre,
            "ROL": rol,
            "SEMESTRE": semestre
        }) #Guarda el diccionario, con los datos que proporcionaste, en la lista integrantes 
        print("Integrante agregado correctamente.")
    else:
        print("Registro descartado.")

