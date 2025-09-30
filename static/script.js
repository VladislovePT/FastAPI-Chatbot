
document.addEventListener("DOMContentLoaded", () => {
    const loginContainer = document.getElementById("login-container");
    const chatContainer = document.getElementById("chat-container");
    const loginButton = document.getElementById("login-button");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const loginError = document.getElementById("login-error");

    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    loginButton.addEventListener("click", login);

    function login() {
        const username = usernameInput.value;
        const password = passwordInput.value;

        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username: username, password: password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                loginContainer.style.display = "none";
                chatContainer.style.display = "flex";
            } else {
                loginError.innerText = data.message;
            }
        });
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value;
        if (message.trim() === "") return;

        appendMessage(message, "user");
        userInput.value = "";

        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            appendMessage(data.response, "bot");
        });
    }

    function appendMessage(message, sender) {
        const messageWrapper = document.createElement("div");
        messageWrapper.classList.add(sender === "user" ? "user-message" : "bot-message");
        
        const messageElement = document.createElement("div");
        messageElement.classList.add("message");
        messageElement.innerText = message;
        
        messageWrapper.appendChild(messageElement);
        chatBox.appendChild(messageWrapper);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
