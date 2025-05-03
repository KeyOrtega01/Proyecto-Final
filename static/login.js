document.getElementById("login-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ "username": email, "password": password })
    });

    const data = await response.json();

    if (response.ok && data.access_token) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "index.html";  // Redirige al usuario tras login exitoso
    } else {
        document.getElementById("mensaje-error").innerText = "Usuario o contraseña incorrectos.";
    }
});
