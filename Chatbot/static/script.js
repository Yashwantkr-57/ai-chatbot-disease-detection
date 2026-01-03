function sendMessage() {
    let input = document.getElementById("userInput");
    let msg = input.value.trim();

    if (msg === "") return;

    let chatBox = document.getElementById("chatBox");

    // User bubble
    let userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.innerText = msg;
    chatBox.appendChild(userDiv);

    input.value = "";

    // Typing indicator
    let typing = document.createElement("div");
    typing.className = "bot typing";
    typing.innerText = "Bot is typing...";
    chatBox.appendChild(typing);

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "msg=" + encodeURIComponent(msg)
    })
    .then(res => res.json())
    .then(data => {
        chatBox.removeChild(typing);

        let botDiv = document.createElement("div");
        botDiv.className = "bot";
        botDiv.innerText = data;
        chatBox.appendChild(botDiv);
    });
}
