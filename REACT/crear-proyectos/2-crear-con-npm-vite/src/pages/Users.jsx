import { useEffect, useState } from "react";
import api from "../api/axios";

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/users")
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error("Error al obtener usuarios:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Cargando...</p>;

  return (
    <div>
      <h1>Usuarios</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
