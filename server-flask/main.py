from flask import Flask
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def obtener_datos_db(query):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Cafeteria"
    )
    
    # Usamos dictionary=True para que el cursor devuelva diccionarios {'columna': valor}
    # en lugar de tuplas indexadas (valor1, valor2)
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(query)
    
    resultados = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    return resultados

@app.route("/")
def hola():
    return "hola mundo"


@app.route("/api/frutas")
def get_fruta():
    return{
        "frutas": ["manzana 1","manzana 2","manzana 3","manzana 4","manzana 5"]
    }

@app.route("/api/usr")
def get_usr():
    return{
        "usuarios": [
            {
                "id": 1,
                "name": "user 1"
            },
            {
                "id": 2,
                "name": "user 2"
            },
            {
                "id": 3,
                "name": "user 3"
            },
            {
                "id": 4,
                "name": "user 4"
            },
        ]
    }


@app.route("/api/menu")
def get_menu():
    try:
        
        productos = obtener_datos_db("SELECT * FROM productos")

        return{
            "menu": productos
        }
    except Exception as e:
        return {"error": f"no se pudo conectar a la base de datos:{str(e)}"}, 500


if __name__ == "__main__":
    app.run(debug=True)