from flask import Flask, render_template, redirect, url_for
import mysql.connector
from collections import defaultdict
from datetime import datetime
import os

app = Flask(__name__)


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

Consulta = obtener_datos_db("SELECT * FROM `productos`ORDER BY FIELD(categoria, 'Plato principal', 'Complemento', 'Postre', 'Bebida', 'Alcohol'), disponibles DESC, id_producto ASC")
#Consulta = obtener_datos_db("SELECT * FROM `productos` ORDER BY `disponibles` DESC, `id_producto` ASC")
#Consulta = obtener_datos_db("SELECT * FROM productos")
#Consulta = obtener_datos_db("SELECT * FROM productos WHERE `stock` > 0")

# 1. Tu array (lista) de entradas fijas con sus valores numéricos
ENTRADAS = Consulta

# 2. El array/diccionario global que almacena cuántas veces se presionó cada botón
# Estructura inicial: {id_entrada: cantidad_de_clics}
historial_clics = {entrada["id_producto"]: 0 for entrada in ENTRADAS}

# Variables para guardar el resultado del cálculo final
ultimo_total = None
mostrar_resultado = False

@app.route("/")
def index():

    productos_agrupados = defaultdict(list)
    for entrada in ENTRADAS:
        productos_agrupados[entrada["categoria"]].append(entrada)
    # Calculamos el total acumulado actual solo para mostrarlo en la interfaz si deseas
    return render_template(
        "index.html", 
        entradas=ENTRADAS, 
        clics=historial_clics,
        total=ultimo_total,
        mostrar_resultado=mostrar_resultado
       
    )

@app.route("/presionar/<int:entrada_id>")
def presionar_boton(entrada_id):
    global mostrar_resultado
    mostrar_resultado = False # Oculta el cartel del total anterior si se vuelve a clickear
    
    # Incrementa el contador del botón específico
    producto_seleccionado = next((p for p in ENTRADAS if p["id_producto"] == entrada_id), None)
    
    if producto_seleccionado and producto_seleccionado["disponibles"] != 0:
        if entrada_id in historial_clics:
            historial_clics[entrada_id] += 1

    return redirect(url_for("index"))

@app.route("/vaciar")
def vaciar_lista():
    global mostrar_resultado, ultimo_total
    mostrar_resultado = False
    ultimo_total = None
    
    # Reinicia todos los contadores a cero
    for entrada_id in historial_clics:
        historial_clics[entrada_id] = 0
        
    return redirect(url_for("index"))

@app.route("/sumar")
def sumar_y_limpiar():
    global ultimo_total, mostrar_resultado
    
    total = 0
    lineas_pedido =[]


    print(f"\nrecibo")

    # Suma el valor numérico de cada fila multiplicado por las veces que se presionó
    for entrada in ENTRADAS:
        cantidad = historial_clics[entrada["id_producto"]]

        if cantidad > 0:
            subtotal = entrada["precio"] * cantidad
            total += subtotal

            print(f"-{entrada['nombre']} x {cantidad} -> ${subtotal}")
        
        

    print(f"{total}")
    
    carpeta_pedidos = "pedidos"
    if not os.path.exists(carpeta_pedidos):
        os.makedirs(carpeta_pedidos)

    numero_pedido = len(os.listdir(carpeta_pedidos)) + 1

    ahora = datetime.now()
    fecha_str = ahora.strftime("%d-%m-%Y")
    hora_str = ahora.strftime("%H-%M-%S")

    nombre_archivo = f"[{numero_pedido}, {total}, {fecha_str}, {hora_str}].txt"
    ruta_completa = os.path.join(carpeta_pedidos, nombre_archivo)

    with open(ruta_completa, "w", encoding="utf-8") as archivo:
        #archivo.write(f"{numero_pedido}\n")
        #archivo.write(f"{ahora.strftime("%d/%m/%Y")}, {ahora.strftime("%H-%M-%S")}")


        #archivo.write(f"\nrecibo")
        archivo.write(f"cant.    descripcion    P.unidad    Total\n")
    # Suma el valor numérico de cada fila multiplicado por las veces que se presionó
        for entrada in ENTRADAS:
            cantidad = historial_clics[entrada["id_producto"]]
            
            if cantidad > 0:
               

                #archivo.write(f"-{entrada['nombre']} x {cantidad} -> ${subtotal}")
                
                archivo.write(f"{cantidad}        {entrada['nombre']} {entrada['precio']} ${subtotal}\n")



        for linea in lineas_pedido:
            archivo.write(linea + "\n")

        archivo.write(f"        Total ${total}\n")
    
    # Guarda el resultado para la interfaz web
    ultimo_total = total
    mostrar_resultado = True
    
    # Limpia el array de clics volviendo todo a cero
    for entrada_id in historial_clics:
        historial_clics[entrada_id] = 0
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
