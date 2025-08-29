# VEX ROBOTICS - GESTOR DE PROYECTOS
#INICIO DEL PROGRAMA 
#MENÚ
print("="*45)
print("\t BINVENIDO A VEX: ROBOTICS")
print("\t\t-----MENÚ-----")
print("="*45)
print("1. Lista de integrantes por sector")
print("2. Inventario/Materiales")
print("3. Lista de pendientes")
print("4. Barra de progreso")
print("5. Salir")
opcion = input("Seleccione una opción: ")

#condicional
if opcion == 1:
#Menu del area de integrantes
print("1.1 Ver la lista de integrantes")
print("1.2 Agregar inegrantes")
opcion1 = input ("Seleccione una opción: ")
#Lista de integrantes 
nombre=""
Listadeinegrantes = "1-" + str(nombre)
# Integrantes por sector
# Preguntar nombres de integrantes de Administración
administracion = input("Escribe los integrantes del sector Administración (separados por coma): ")
# Preguntar nombres de integrantes de Mecánica
mecanica = input("Escribe los integrantes del sector Mecánica (separados por coma): ")
# Preguntar nombres de integrantes de Programación
programacion = input("Escribe los integrantes del sector Programación (separados por coma): ")
#agg integrante a cualquier seccion
nuevo_integrante= input("Deseas agregar un integrante nuevo (s/n)")
if nuevo_integrante == "s":
     input("Escribe aqui el nombre del nuevo integrante->")

elif opcion == 2:
# -------------------------------
#variables de materiales 
Motores=0
Cerebros=0
Cable=0
Tornillos=0
Tuercas=0
Arandelas=0
Baterias=0
Canales=0
Placas_Acero=0
Chasis_Acero=0
Barras_Acero=0
Steel_Angles=0
CCanales_Acero=0
Refuerzos_Acero=0
Engranajes=0
Rodillos=0
Embragues=0
Collares=0
Ejes=0
Separadores=0
Espaciadores=0




# Inventario de materiales
# Preguntar materiales disponibles
materiales = input("Escribe los materiales con sus cantidades (ejemplo: Tornillos=50, Motores=2): ")

#opcion de agregar o eliminar materiales
agregarMaterial= input ("Desea agregar material al invenario?(s/n)")
if agregarMaterial =="s":
    input("Escribe el nombre del material que desea agregar")

sacarMaterial= input("Desea sacar material del inventario?(s/n)")
if sacarMaterial=="s":
    input("Escribe el nombre del material que se desea sacar")
 
# Lista de pendientes: lista de tareas con su estado ()
elif ocion ==3 
pendientes = (
    ("Diseñar prototipo", False),
    ("Programar sensores", True),
    ("Revisar baterías", False)
)


# Contar total de tareas()
total_tareas = 0
for tarea in pendientes:
    total_tareas = total_tareas + 1

# Contar tareas completadas
tareas_completadas = 0
for tarea in pendientes:
    if tarea (1):
        tareas_completadas = tareas_completadas + 1

# Calcular progreso como porcentaje (operacion)
elif opcion ==4
progreso = float(tareas_completadas) / total_tareas * 100
# Mostrar barra de progreso simple ()

#opcion de salir
elif opcion ==5