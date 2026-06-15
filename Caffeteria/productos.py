import mysql.connector

conexion =  mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="Cafeteria"
 )
cursor = conexion.cursor()

cursor.execute("SELECT * FROM Productos")

Productos = cursor.fetchall()

print("\nLista de Productos\n")

for Producto in Productos:
    print(Productos)

    conexion.close()
