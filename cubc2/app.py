from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# 1. Tu array (lista) de entradas fijas con sus valores numéricos
ENTRADAS = [
    {"id": 0, "nombre": "Entrada Alfa", "valor": 10},
    {"id": 1, "nombre": "Entrada Beta", "valor": 25},
    {"id": 2, "nombre": "Entrada Gamma", "valor": 50},
    {"id": 3, "nombre": "Entrada Delta", "valor": 100},
]

# 2. El array/diccionario global que almacena cuántas veces se presionó cada botón
# Estructura inicial: {id_entrada: cantidad_de_clics}
historial_clics = {entrada["id"]: 0 for entrada in ENTRADAS}

# Variables para guardar el resultado del cálculo final
ultimo_total = None
mostrar_resultado = False

@app.route("/")
def index():
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
    # Suma el valor numérico de cada fila multiplicado por las veces que se presionó
    for entrada in ENTRADAS:
        cantidad = historial_clics[entrada["id"]]
        total += entrada["valor"] * cantidad
    
    # Imprime en la consola de Python
    print(f"\n--- CÁLCULO FINAL ---")
    print(f"Resultado de la suma: {total}")
    print(f"----------------------\n")
    
    # Guarda el resultado para la interfaz web
    ultimo_total = total
    mostrar_resultado = True
    
    # Limpia el array de clics volviendo todo a cero
    for entrada_id in historial_clics:
        historial_clics[entrada_id] = 0
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
