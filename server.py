"""
Flask web server for Assist_Bot.
Reuses your existing config.py, chat.py, and history.py — no backend logic changed.

Run:
    pip install flask
    python server.py

Then open http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, jsonify

from config import get_working_model
from chat import chat
from history import load_history, save_history, clear_history
import json

app = Flask(__name__)

model = get_working_model()
history = load_history()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    global history

    data = request.get_json(silent=True) or {}
    user_msg = (data.get("message") or "").strip()

    if not user_msg:
        return jsonify({"error": "Empty message"}), 400

    # chat() prints to stdout (streaming) and returns the updated history list,
    # where the last entry is "AI Tutor : <full reply>"
    history = chat(model, history, user_msg)
    save_history(history)

    last_entry = history[-1]
    reply = last_entry.split("AI Tutor : ", 1)[-1].strip()

    return jsonify({"reply": reply})


@app.route("/clear", methods=["POST"])
def clear_endpoint():
    global history
    clear_history()
    history = []
    return jsonify({"status": "cleared"})

@app.route("/history")
def get_history():
    data=load_history()
    return data


if __name__ == "__main__":
    app.run(debug=True)
