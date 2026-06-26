from flask import Flask, render_template
import requests

app = Flask(__name__)

BOT_INVITE = "https://discord.com/oauth2/authorize?client_id=1398895385711349822&permissions=8&scope=bot"

@app.route("/")
def home():
    try:
        data = requests.get(
            "https://discord-bot-production-cc86.up.railway.app/stats",
            timeout=5
        ).json()

        server_count = data.get("servers", 0)

    except Exception:
        server_count = "Offline"

    return render_template(
        "index.html",
        bot_invite=BOT_INVITE,
        server_count=server_count
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
