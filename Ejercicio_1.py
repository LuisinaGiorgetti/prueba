ingredientes=['Harina','Azucar','Leche','Huevos','Ralladura de limón']
op = -1
while (op!=0):
    print("Lista de ingredientes")
    print(ingredientes)
    print()
    print("Menú principal")
    print("1- Eliminar un elemento")
    print("2- Agregar un elemento")
    print("0- Salir")
    while True:
        op=int(input("Ingrese una opción"))
        if (op<0) or (op>2):
            print("La opción no es válida")
        else:
            break
    if (op==1):
        ingrediente=input("Ingresar ingrediente a borrar")
        if (ingrediente in ingredientes):
            ingredientes.remove(ingrediente)
        else:
            print("No existe ese ingrediente")
    if (op==2):
        ingrediente=input("Ingresar ingrediente a agregar")
        if (ingrediente in ingredientes):
            print("Ya existe ese ingrediente")
        else:
            ingredientes.append(ingrediente)
