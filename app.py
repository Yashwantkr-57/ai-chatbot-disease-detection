from flask import Flask, render_template, request, jsonify
from Chatbot.decision import process_message
from Chatbot.database import init_db


app = Flask(
    __name__,
    template_folder="Chatbot/templates",
    static_folder="Chatbot/static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"]

    print("User:", user_msg)
    response = process_message(user_msg)
    print("Bot:", response)

    return jsonify(response)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

