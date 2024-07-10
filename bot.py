from pyrogram import Client
import config
from plugins import commands, pmfilter

# Initialize the bot
app = Client(
    "bot",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

# Register command handlers
commands.register_commands(app)

# Register PM filter
pmfilter.register_pmfilter(app)

if __name__ == "__main__":
    # Start the bot
    app.run()
