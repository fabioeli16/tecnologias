// DependencyEffect.jsx
//El efecto solo se ejecuta cuando contador cambia y al primer render
import { useEffect, useState } from "react";

function DependencyEffect() {
  const [contador, setContador] = useState(0);

  useEffect(() => {
    console.log("DependencyEffect → contador cambió:", contador);
  }, [contador]);

  return (
    <div>
      <h3>DependencyEffect</h3>
      <p>Contador: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
    </div>
  );
}

export default DependencyEffect;
