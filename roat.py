listalibros=[];
encabezado=[];
matrizDatos=[];
import csv
#Agregar lista de los libros

def agregar_libros():
    libros=int(input("Ingrese el nombre del libro ---> "));
    listalibros.append(libros);
    print("Se ingreso correctamente el libro");
    return libros
#ver lista de libros

def mostrarlibros():
    print(f"La lista de trabajadores es ---> {listalibros}");
    return mostrarlibros

#eliminar los libros

def eliminar_libros():
    listalibros=[];
    libros=int(input("Ingrese el nombre del libro que desea remover o eliminar ---> "));
    listalibros.remove(libros);

#Guardar coleccion en un archivo

def guardar_archivo():
    listalibros=[];
    print("ingrese nombre del archivo");
    listalibros.__add__(__file__);
    print("Se agrego correctamente el archivo");

with open('datos_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
    archivo_csv=csv.writer(archivo_csv);
    archivo_csv.writerow(encabezado);
    archivo_csv.writerow(matrizDatos);
    print("Se creo el archivo correctamente.");
    
    
