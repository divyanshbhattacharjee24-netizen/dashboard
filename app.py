from flask import Flask

app = Flask(__name__)

BOT_INVITE = "https://discord.com/oauth2/authorize?client_id=1398895385711349822&permissions=8&scope=bot"

@app.route("/")
def home():
    return f"""
    <h1>Roblox Fans Mod</h1>
    <p>Modmail • Applications • Moderation</p>
    <a href="{BOT_INVITE}">
        <button>Invite Bot</button>
    </a>
    """
