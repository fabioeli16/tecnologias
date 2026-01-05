// MountEffect.jsx
// Se ejecuta una sola vez, al primer render
import { useEffect } from "react";

function MountEffect() {
  useEffect(() => {
    console.log("MountEffect → solo al montar el componente");

    return () => {
      console.log("MountEffect → limpieza al desmontar");
    };
  }, []);

  return (
    <div>
      <h3>MountEffect</h3>
      <p>Revisa la consola</p>
    </div>
  );
}

export default MountEffect;
