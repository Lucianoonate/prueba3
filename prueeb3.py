pedi = []
def registrapedi():
    nombre_cliente = input("Nombre del cliente: ")
    apellido_cliente = input("Apellido del cliente: ")
    comuna = input("ingrese la comuna: ")

    cantidad5kg = int(input("Cantidad de cilindros de 5kg: "))
    cantidad15kg = int(input("Cantidad de cilindros de 15kg: "))
    cantidad45kg = int(input("Cantidad de cilindros de 45kg: "))

pedidos.append(detalle_pedido)

def imprimir_hoja():
    print("\n--- Sectores Disponibles para Hoja de Ruta ---")
    for i, sector in enumerate(sectores_disponibles, start=1):
        print(f"{i}. {sector}")

def listar_pedidos():
    if
def menupedido()
    while(True):
        print "bienvenido al sistema de pedidos tu espacio"
        print "1. Registrar pedido"
        print "2. Listar todos los pedidos"
        print "3. Imprimir hoja de ruta"
        print "4. salir del programa"

        try:
            opcion = int(input("Ingrese una opción"))

        if opcion == 1
        registrapedi()
        elif opcion == 2
        
        elif opcion == 3
        imprimir_hoja()
        elif opcion == 4
        print "Adios!"
        break
    else:
    print("opcion no válida, porfavor ingrese una opcion de 1 a la 4")
    
    except ValueError as e:
     print(f"Error, Por favor, ingrese valores numéricos válidos.")