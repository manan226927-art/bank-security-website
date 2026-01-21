function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;
    let status = document.getElementById("status");

    status.innerHTML = "🧠 Encrypting credentials...";
    
    setTimeout(() => {
        status.innerHTML = "🔐 Verifying bank security...";
    }, 1000);

    setTimeout(() => {
        if (user === "student" && pass === "1234") {
            status.innerHTML = "✅ ACCESS GRANTED";
            setTimeout(() => {
                window.location.href = "/bank-form";
            }, 800);
        } else {
            status.innerHTML = "❌ ACCESS DENIED";
        }
    }, 2000);
}