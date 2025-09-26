def agregar_inventario():
    archivo=open("inventario.txt","+a")
    try:
        numero=int(input("¿Cuantos objetos desea registrar?"))
        for i in range(numero):
            objeto=input("¿Objeto que desea registrar?")
            cantidad=input("¿Numero de existencias?")
            archivo.write("Objeto = "+objeto.title()+",--- Cantidad = "+cantidad+"\n") 
    except ValueError:
        print("Ingrese un valor numerico ")
def consultar_inventario():
    with open("inventario.txt","r") as archivo:
        for line in archivo:
            print(line)
def modificar_inventario():
    with open("inventario.txt","r+") as archivo:
        inventario=[]
        for line in archivo:
            inventario.append(line.split(","))
        busqueda=input("¿Objeto que desea modificar?")
        for i in range(len(inventario)):
            if inventario[i][0]=="Objeto = "+busqueda.title():
                modif=input("¿Cantidad actual?")
                inventario[i][1]=",--- Cantidad = "+modif+"\n"
            elif i==(len(inventario)-1):
                print("Objeto no encontrado")
    archivo=open("inventario.txt","w")
    for i in range(len(inventario)):  
         archivo.write(inventario[i][0]+","+inventario[i][1])
def menu_inventario():
    while True:
        print("---INVENTARIO---\n1.Consultar inventario\n2.Agregar objetos al inventario\n3.Modificar las existencias de un objeto en el inventario\n4.Salir")
        try:        
            res=int(input("Selecciona una opción (1-4):"))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        else:
            if res==1:
                try:
                    consultar_inventario()
                except FileNotFoundError:
                    print("No existe archivo inventario, elija agregar inventario")
            elif res==2:
                try:
                    agregar_inventario()
                except FileNotFoundError:
                    archivo=open("inventario.txt","w")
                    agregar_inventario()
            elif res==3:
                try:
                    modificar_inventario()
                except FileNotFoundError:
                    print("No existe archivo inventario, elija agregar inventario")
            elif res==4:
                break
            else:
                print("Opcion no valida")