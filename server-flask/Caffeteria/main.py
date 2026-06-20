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



def conexion_fix(query): 
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
        #remplace Productos por Producto
        if query.strip().upper().startswith(("UPDATE", "INSERT", "DELETE")):
            conexion.commit()
            
        #cierre de conexion
        conexion.close()

def autofixtable():
#SELECT * FROM `Productos` WHERE `stock` = 0 || `disponibles` = 0; 
    conexion_fix("UPDATE `Productos` SET `disponibles`= 1 WHERE `stock` > 0")
    conexion_fix("UPDATE `Productos` SET `disponibles`= 0 WHERE `stock` < 1")





def categoriaprint():
    
    while True:    
        print("\n==== Seleccione una Categoria ====")
        print("1. Bebidas")
        print("2. Alimentos")
        print("3. Cócteles")
        print("4. Cupcakes")
        print("5. Entrada")
        print("6. Platillo Fuerte")
        print("7. Roles de Canela")
        print("8. Snack")
        print("9. cancelar")
        
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
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Cócteles'")
            case "4":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Cupcakes'")
            case "5":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Entrada'")
            case "6":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Platillo Fuerte'")
            case "7":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Roles de Canela'")
            case "8":
                print("\033[H\033[J", end="")
                conexion("SELECT * FROM `productos` WHERE `categoria` = 'Snack'")
            case "9":
                print("\033[H\033[J", end="")            
                break
            case _:
                print("\033[H\033[J", end="")        
                print("Opción no válida, por favor intente de nuevo")
            


while True:
    
    autofixtable()

    print("\n==== Bienvenido a la Cafeteria ====")
    print("1. Ver Productos")
    print("2. productos de categoria especifica")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    print("\033[H\033[J", end="")
    

    match opcion:
        case "1":
            submenu1 = True


            while submenu1:
                
                print("1. ver todos los productos")
                print("2. ver solo productos disponibles")
                print("3. cancelar")
                sm1_opcion = input("Seleccione una opción: ")

                match sm1_opcion:
                    case "1":
                        print("\033[H\033[J", end="")   
                        conexion("SELECT * FROM Productos")
                    case "2":
                        print("\033[H\033[J", end="")   
                        conexion("SELECT * FROM Productos WHERE disponibles = 1")
                    case "3":
                        print("\033[H\033[J", end="")
                        break
                    case _:
                        print("\033[H\033[J", end="")
                        print("Opción no válida, por favor intente de nuevo")
            


           
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

 
