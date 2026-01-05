// App.jsx
import RenderEffect from "./RenderEffect";
import MountEffect from "./MountEffect";
import DependencyEffect from "./DependencyEffect";

function App() {
  return (
    <div>
      <h2>Ejemplos de useEffect</h2>

      <RenderEffect />
      <hr />

      <MountEffect />
      <hr />

      <DependencyEffect />
    </div>
  );
}

export default App;
