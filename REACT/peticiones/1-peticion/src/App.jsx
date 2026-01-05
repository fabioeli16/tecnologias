import { useState } from "react";

function App() {
  // Estado para guardar los datos de la API
  const [users, setUsers] = useState([]);
  // Estado para saber si ya se hizo la petición
  const [loaded, setLoaded] = useState(false);

  const fetchUsers = async () => {
    try {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/users"
      );
      const data = await response.json();
      setUsers(data);
      setLoaded(true);
    } catch (error) {
      console.error("Error al consumir la API", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Usuarios</h1>

      <button onClick={fetchUsers}>
        Cargar usuarios
      </button>

      {loaded && (
        <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Email</th>
              <th>Ciudad</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.address.city}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;

