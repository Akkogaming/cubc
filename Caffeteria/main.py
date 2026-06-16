import mysql.connector


print("\033[H\033[J", end="")

#definir el menu antes que nada para que el resto del programa pueda leerlo
def conexion(query): 
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

        cursor.execute(query)


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

def categoriaprint():
    
    while True:    
        print("\n==== Seleccione una Categoria ====")
        print("1. Bebidas")
        print("2. Alimentos")
        print("3. cancelar")
        
        categoria = input("Seleccione una opción: ")

        match categoria:
            case "1":
                print("\033[H\033[J", end="")                
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Bebida'")
                #SELECT * FROM `productos` WHERE `categoria` = 'Bebida'; 
            case "2":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Alimento'")
            case "3":
                print("\033[H\033[J", end="")            
                break
            case _:
                print("\033[H\033[J", end="")        
                print("Opción no válida, por favor intente de nuevo")
            


while True:
    
    print("\n==== Bienvenido a la Cafeteria ====")
    print("1. Ver Productos")
    print("2. productos de categoria especifica")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\033[H\033[J", end="")
            conexion("SELECT * FROM Productos")
        case "2":
              print("\033[H\033[J", end="")
              categoriaprint()
        case "3":
            print("\033[H\033[J", end="")            
            break
        case _:
            print("\033[H\033[J", end="")
            print("Opción no válida, por favor intente de nuevo")


print("Gracias por visitar la Cafeteria")

















   # if opcion == "1":
  #      part1()

   # elif opcion == "2":
   #     print("Gracias por visitar la Cafeteria")
    #    break
    
   # else:
    #    print("Opción no válida, por favor intente de nuevo")

 
