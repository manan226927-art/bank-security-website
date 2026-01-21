let texts = [
    "🧠 Scanning neural network...",
    "🔍 Checking suspicious activity...",
    "🛡️ Blocking threats...",
    "🔐 Encrypting bank data...",
    "✅ System fully secure"
];

let i = 0;
let aiText = document.getElementById("aiText");

setInterval(() => {
    aiText.innerHTML = texts[i];
    i = (i + 1) % texts.length;
}, 1500);