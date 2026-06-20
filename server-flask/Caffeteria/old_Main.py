import mysql.connector

#definir el menu antes que nada para que el resto del programa pueda leerlo
def conexion():
        #se establece la conexion con la base de datos
        conexion =  mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Cafeteria"
        )

        #la verdad no se que es un cursor pero parece que es como el "statement.execute(query)" de java
        cursor = conexion.cursor()
        #este ejecuta la consulta
        cursor.execute("SELECT * FROM Productos")
        #guarda todos los datos que la consulta dio en la variable productos
        Productos = cursor.fetchall()
        #encabezado
        print("\n---Productos Disponibles ---")
        #remplace Productos por Producto
        for Producto in Productos:
            #aqui
            #al tener productos imprimia todos los elementos en una fila con tantas filas como haya
            print(Producto)
        #cierre de conexion
        conexion.close()

while True:
    
    print("\nBienvenido a la Cafeteria ====")
    print("1. Ver Productos")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            conexion()
        case "2":
            break
        case _:
            print("Opción no válida, por favor intente de nuevo")

print("Gracias por visitar la Cafeteria")

















   # if opcion == "1":
  #      part1()

   # elif opcion == "2":
   #     print("Gracias por visitar la Cafeteria")
    #    break
    
   # else:
    #    print("Opción no válida, por favor intente de nuevo")

 
