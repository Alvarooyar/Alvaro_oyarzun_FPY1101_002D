import roat as funcion
#listas
listalibros=[];
encabezado=[];
matrizDatos=[];
#Menu de opciones
print("----- Bienvenidos a nuestra biblioteca Duoc Uc -----");
print("");
while True:
    print("1.-Agregar un libro");
    print("");
    print("2.-Ver todos los libros");
    print("");
    print("3.-modificar un libro");
    print("");
    print("4.-eliminar un libro de la lista");
    print("");
    print("5.-guardar coleccion en un archivo");
    print("");
    print("6.- Salir del programa");
    print("");

    try:
        opcion=int(input("Seleccione una opcion --> "));
    except:
        print("respuesta invalida, intentelo de nuevo.");

    if opcion==1:
        print("Usted selecciono la opcion de agregar libros");
        libros=int(input("Ingrese el nombre del libro ---> "));
        listalibros.append(libros);
        print("Se ingreso correctamente el libro");
        funcion.agregar_libros();
        print("");

    elif opcion==2:
        print("Usted selecciono la opcion de ver todos los libros");
        funcion.mostrarlibros();
        print("");

    elif opcion==3:
        print("Usted ingreso la opcion modificar libro")

    elif opcion==4:
        print("Usted selecciono la opcion de eliminar un libro de la lista");
    elif opcion==5:
        print("saliendo del programa");
        break
    else:
        print("Respuesta erronea. Vuelva a intentarlo...");

