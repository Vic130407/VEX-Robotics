# VEX ROBOTICS - GESTOR DE PROYECTOS
#INICIO DEL PROGRAMA 
#MENÚ
print("1. Lista de integrantes por sector")
print("2. Inventario/Materiales")
print("3. Lista de pendientes")
print("4. Barra de progreso")
print("5. Salir")
opcion = input("Seleccione una opción: ")

# Integrantes por sector
# Preguntar nombres de integrantes de Administración
administracion = input("Escribe los integrantes del sector Administración (separados por coma): ")
# Preguntar nombres de integrantes de Mecánica
mecanica = input("Escribe los integrantes del sector Mecánica (separados por coma): ")
# Preguntar nombres de integrantes de Programación
programacion = input("Escribe los integrantes del sector Programación (separados por coma): ")

# -------------------------------
#variables de materiales 

# Inventario de materiales
# Preguntar materiales disponibles
materiales = input("Escribe los materiales con sus cantidades (ejemplo: Tornillos=50, Motores=2): ")

# Lista de pendientes: lista de tareas con su estado ()
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
progreso = float(tareas_completadas) / total_tareas * 100
# Mostrar barra de progreso simple ()