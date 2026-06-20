import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  // 1. Declaramos la variable "productos" y su función para actualizarla "setProductos"
  const [productos, setProductos] = useState([])

  useEffect(() => {
    fetch("http://localhost:5000/api/menu")
      .then((res) => res.json())
      .then((data) => {
        // Tu servidor de Flask devuelve {"menu": [...]}, así que accedemos a data.menu
        setProductos(data.menu)
      })
      .catch((error) => console.error("Error al traer el menú:", error));
  }, []); // El array vacío evita que se ejecute infinitamente

  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="framework" alt="React logo" />
          <img src={viteLogo} className="vite" alt="Vite logo" />
        </div>
        
        <div>
          <h1>Menú de la Cafetería</h1>
          
          <div className='card'>
            {/* 2. Si no hay productos todavía, mostramos un mensaje de carga */}
            {productos.length === 0 ? (
              <p>Cargando productos...</p>
            ) : (
              // 3. Usamos .map() para iterar sobre la lista de productos de la base de datos
              productos.map((prod) => (
                <div key={prod.id_producto} style={{ margin: '15px 0', borderBottom: '1px solid #333', paddingBottom: '10px' }}>
                  
                  {/* Corregido: "nomre" cambiado a "nombre" */}
                  <h3>{prod.nombre}</h3>

                  <p>Categoría: {prod.categoria} | Precio: ${prod.precio}</p>

                  <small style={{ color: prod.stock > 0 ? "#4caf50" : "#f44336" }}>
                    Stock disponible: {prod.stock} unidades
                  </small>
                  
                </div>
              ))
            )}
          </div>
        </div>
      </section>

      <div className="ticks"></div>
      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App