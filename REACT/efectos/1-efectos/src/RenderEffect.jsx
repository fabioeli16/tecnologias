// RenderEffect.jsx
// El useEffect se ejecuta en cada renderizado
import { useEffect, useState } from "react";

function RenderEffect() {
  const [contador, setContador] = useState(0);

  useEffect(() => {
    console.log("RenderEffect → se ejecuta en cada render");
  });

  return (
    <div>
      <h3>RenderEffect</h3>
      <p>Contador: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
    </div>
  );
}

export default RenderEffect;
