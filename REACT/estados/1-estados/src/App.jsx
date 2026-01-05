import { useState, useRef } from "react";

function App() {

  // Estado contador inicializado en 0
  const [contador, setContador] = useState(0);

  // Ref para contar renders
  const renders = useRef(0);
  // Se incrementa en cada render
  renders.current++;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Ejemplo de estado en React</h1>

      <p>Contador: {contador}</p>
      <p>cantidad de Renders: {renders.current}</p>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>

      <button onClick={() => setContador(contador - 1)}>
        Decrementar
      </button>

      <button onClick={() => setContador(0)}>
        Reset
      </button>
    </div>
  );
}



export default App;