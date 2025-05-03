document.getElementById("registro-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/registro", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, email, password })
    });

    const data = await response.json();

    if (response.ok) {
        alert("¡Registro exitoso! Ahora puedes iniciar sesión.");
        window.location.href = "login.html";  // Redirige al usuario después del registro
    } else {
        document.getElementById("mensaje-error").innerText = data.detail || "Error en el registro.";
    }
});
